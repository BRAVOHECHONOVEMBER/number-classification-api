from fastapi import FastAPI\napp = FastAPI()\n@app.get('/')\ndef home(): return {'message': 'Welcome to the Number Classification API'}
