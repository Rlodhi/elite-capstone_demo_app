from fastapi import FastAPI

app = FastAPI(
    title="EliteA Capstone Demo Application",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "application": "EliteA Capstone Demo Application",
        "status": "running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.get("/api/application")
def application_info():
    return {
        "name": "EliteA Capstone Demo Application",
        "version": "1.0.0",
        "framework": "FastAPI"
    }
