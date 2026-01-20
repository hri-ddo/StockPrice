
import gradio as gr
import pandas as pd
import joblib
model = joblib.load('stock_model.pkl')

def predict_stock(date_str, stock_2, stock_3, stock_4, stock_5):
    try:
        date_obj = pd.to_datetime(date_str)
        month = date_obj.month
        day = date_obj.day
        day_of_week = date_obj.dayofweek
  
        competitor_mean = (stock_2 + stock_3 + stock_4 + stock_5) / 4.0
        input_data = pd.DataFrame([[
            stock_2, stock_3, stock_4, stock_5, 
            month, day, day_of_week, competitor_mean
        ]], columns=['Stock_2', 'Stock_3', 'Stock_4', 'Stock_5', 'Month', 'Day', 'DayOfWeek', 'Competitor_Mean'])

        prediction = model.predict(input_data)[0]
        
        return f"Predicted Stock_1 Price: {prediction:.2f}"
    except Exception as e:
        return f"Error: {str(e)}"

# Create Gradio Interface
iface = gr.Interface(
    fn=predict_stock,
    inputs=[
        gr.Textbox(label="Date (YYYY-MM-DD)", value="2020-01-01"),
        gr.Number(label="Stock 2 Value", value=100.0),
        gr.Number(label="Stock 3 Value", value=100.0),
        gr.Number(label="Stock 4 Value", value=100.0),
        gr.Number(label="Stock 5 Value", value=100.0),
    ],
    outputs="text",
    title="Stock Price Prediction App",
    description="Enter the date and competitor stock values to predict Stock 1 price."
)

# Launch the app
iface.launch() 