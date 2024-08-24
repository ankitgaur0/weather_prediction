from flask import Flask,request,render_template
from src.pipeline.test_pipeline import Custom_data,predict_pipeline


app=Flask("__name__")

#make a route to associate it with home page
@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/predict",methods=['GET','POST'])
def predict_datapoints():
    if request.method == "GET":
        return render_template("form.html")
    else:
        DATA=Custom_data(
                 Temperature=request.form.get("Temperature"),
                 Humidity= request.form.get("Humidity"),
                 Wind_Speed =request.form.get("Wind_Speed"),
                 Precipitation =request.form.get("Precipitation"),
                 Cloud_Cover =request.form.get("Cloud_Cover"),
                 Atmospheric_Pressure =request.form.get("Atmospheric_Pressure"),
                 UV_Index =request.form.get("UV_Index"),
                 Season =request.form.get("Season"),
                 Visibility_km =request.form.get("Visibility_km"),
                 Location =request.form.get("Location")
        )
        #now convert into the DataFrame by the function 
        df=DATA.get_data_DataFrame()

        predict_obj=predict_pipeline()
        pred=predict_obj.predict_target(df)

        result=pred
        return render_template("result.html",final_result=result)
    

if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0', port=8080)