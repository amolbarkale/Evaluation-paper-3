from langchain_community.document_loaders import CSVLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_qdrant import QdrantVectorStore

# document loader
loader = CSVLoader(file_path='./dailyActivity_merged.csv',
    csv_args={
    'delimiter': ',',
    'quotechar': '"',
    'fieldnames': ['Id','ActivityDate','TotalSteps','TotalDistance','TrackerDistance','LoggedActivitiesDistance','VeryActiveDistance','ModeratelyActiveDistance','LightActiveDistance','SedentaryActiveDistance','VeryActiveMinutes','FairlyActiveMinutes','LightlyActiveMinutes','SedentaryMinutes','Calories']
})

csv = loader.load()
print(csv[0].page_content[:100])
print(csv[0].metadata)

# chunking
text_split = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap= 200
)
text_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size=100,
    chunk_overlap=20,
)
# recursive split
docs = text_splitter.create_documents(docs=csv)

# embedding model
embedding_model = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")

# Qdrant vector store
vector_store = QdrantVectorStore.add_documents(
    url="http://localhost:6333/",
    collection="daily-tracker",
    embeddings=embedding_model
)

retriever = QdrantVectorStore.from_documents(
    url="http://localhost:6333/",
    collection="daily-tracker",
    embeddings=embedding_model
)

user_query = "what is TotalSteps for 3/25/2016?"

retriever.search(query=user_query)
