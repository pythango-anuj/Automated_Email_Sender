from gui.run_gui import run_gui
from src.db_operations import create_or_update_db


if __name__ == "__main__":
    # Update Database tables
    create_or_update_db()
    # Run the GUI Part
    run_gui()