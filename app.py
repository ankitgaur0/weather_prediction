import Flask,requests,render_template
from src.pipeline.test_pipeline import Custom_data,predict_pipeline


app=Flask("__name__")

#make a route to associate it with home page
@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/predict",methods=['GET','POST'])
def predict_datapoints():
    if requests.method == "GET":
        return render_template("form.html")
    else:
        DATA=Custom_data(
                 Temperature=requests.form.get("Temperature"),
                 Humidity= requests.form.get("Humidity"),
                 Wind_Speed =requests.form.get("Wind_Speed"),
                 Precipitation =requests.form.get("Precipitation"),
                 Cloud_Cover =requests.form.get("Cloud_Cover"),
                 Atmospheric_Pressure =requests.form.get("Atmospheric_Pressure"),
                 UV_Index =requests.form.get("UV_Index"),
                 Season =requests.form.get("Season"),
                 Visibility_km =requests.form.get("Visibility_km"),
                 Location =requests.form.get("Location")
        )
        #now convert into the DataFrame by the function 
        df=DATA.get_data_DataFrame()

        predict_obj=predict_pipeline()
        pred=predict_obj.predict_target(df)

        result=pred
        return render_template("result.html",final_result=result)
