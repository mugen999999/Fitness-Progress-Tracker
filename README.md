
# Fitness Progress Tracker

A simple **Python-based web application** built with **Flask** to log and track fitness progress, including exercises, sets, reps, weight lifted, and workout duration.

## Features
- Log workouts with date, exercise type, sets, reps, weight, and duration
- View past workout history
- Data stored in a CSV file for easy backup
- Simple, intuitive web interface

## Requirements
- Python 3.x
- Flask (installed via `pip`)

## How to Use

1. **Clone this repository**:
   ```bash
   git clone https://github.com/mugen999999/Fitness-Progress-Tracker.git
   cd Fitness-Progress-Tracker
   ```

2. **Create a Virtual Environment** (Optional, but recommended):
   ```bash
   python -m venv venv
   venv\Scripts\activate  # For Windows
   # or
   source venv/bin/activate  # For macOS/Linux
   ```

3. **Install the required dependencies**:
   ```bash
   pip install flask
   ```

4. **Run the Flask App**:
   ```bash
   python app.py
   ```

5. **Access the app**:
   Open a browser and visit:
   ```
   http://127.0.0.1:5000
   ```

6. **Log your workouts**:
   - Add entries with the date, type of exercise, duration, and calories burned.
   - View your workout log below the form.
   
7. **Stored Data**:
   Your workouts are saved in `data/workouts.csv`. This file will be updated each time you log a new workout.

## Customization
- You can modify the CSV storage, add more fields (e.g., body weight, heart rate), or enhance the app's functionality (e.g., add graphs, search filters, etc.).

## Contributing
Feel free to fork this repository, create an issue, or submit a pull request with improvements!
