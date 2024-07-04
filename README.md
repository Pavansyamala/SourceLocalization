# Source Localization Problem Using Deep Learning Models

## Execution Flow of the Method

1. **Create a New Environment:**
   - Open VS Code Terminal and create a new environment using:
     ```bash
     conda create -p venv python=3.9 -y
     ```
     (Replace `python=3.9` with your preferred Python version)

2. **Activate the Environment:**
   - After creating the environment, activate it using:
     ```bash
     conda activate venv/
     ```

3. **Clone the Repository:**
   - Clone this repository using Git:
     ```bash
     git clone https://github.com/Pavansyamala/SourceLocalization.git
     ```

4. **Install Requirements:**
   - Navigate into the cloned repository and install the required packages:
     ```bash
     pip install -r requirements.txt
     ```

5. **About Data Generation**
   - **Before Excution of the following Remeber one thing Just Change the File Path According to Your System in ```bash datageneration.py``` file ```bash line number : 160``` , ```bash variable name : path_todata```**
   - Run the datageneration.py file to create the dataset:
     ```bash
     python datageneration.py
     ```


## Code to use the model 
```bash
   import tensorflow
    from tensorflow.keras.models import load_model
    model = load_model("DL_Models/acc_model")
    prediction = model.predict(test_data)
```

## Format of the Data to be Given to the Model 

- **numpy array of n rows and 9 columns**
- **Where the order of 9 columns are**
  - **Reciever X location** 
  - **Reciever Y location** 
  - **Reciever Z location** 
  - **Magnetic Component along X direction measured by reciever**
  - **Magnetic Component along Y direction measured by reciever**
  - **Magnetic Component along Z direction measured by reciever** 
  - **Reciever Roll Angle**
  - **Reciever Pitch Angle**
  - **Reciever Yaw Angle**
