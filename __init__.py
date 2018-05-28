#coding=utf-8
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def homepage():
    title = "Derek的主页"
    paragraph = [
        "wow this is derek's first Flask homepage!",
        "wow this is derek's first Flask homepage!"]

    try:
        return render_template("index.html", title=title, paragraph=paragraph)
    except Exception as e:
        return str(e)


@app.route('/about')
def aboutpage():
    title = "关于Derek"
    paragraph = ["blah blah blah this is about page"]
    pageType = 'about'
    return render_template("index.html", title=title, paragraph=paragraph, pageType=pageType)


@app.route('/about/contact')
def contactPage():
    title = "联系Derek"
    paragraph = ["blah blah blah Derek Page"]
    pageType = 'contact'
    return render_template("index.html", title=title, paragraph=paragraph, pageType=pageType)


@app.route('/graph')
def graph(chartID='chart_ID', chart_type='line', chart_height=500):
    chart = {"renderTo": chartID, "type": chart_type, "height": chart_height, }
    series = [{"name": 'Label1', "data": [1, 2, 3]}, {"name": 'Label2', "data": [4, 5, 6]}]
    title = {"标题": 'Livechat冒泡邀请展示统计报表'}
    xAxis = {"categories": ['X', 'xAxis Data2', 'xAxis Data3']}
    yAxis = {"title": {"text": 'yAxis Label'}}
    return render_template('index.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis,
                           yAxis=yAxis)


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=8543, passthrough_errors=True)