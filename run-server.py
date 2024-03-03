import sys

# from alembic.config import Config
import alembic
from alembic import command
import uvicorn
import uvicorn.workers
import settings



app = "Backend.settings:app"

if __name__ == "__main__":
    if "--reload" in sys.argv:
        # Running with uvicorn in development mode (with --reload)
        uvicorn.run(app, host="0.0.0.0", port=8002, reload=True)
    else:
        # Running with gunicorn in production mode

        class MyUvicornWorker(uvicorn.workers.UvicornWorker):
            def handle_exit(self, sig, frame):
                # Handle worker exit to close the database connection cleanly
                self.app.setup.shutdown()
                super().handle_exit(sig, frame)


        uvicorn.run(app, host="0.0.0.0", port=8002, workers=4, reload=False ,)
