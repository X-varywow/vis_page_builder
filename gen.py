import json

def gen(df, vis):
    with open (vis, "r") as f:
        d = json.loads(f.read())

    with open("out.html","w", encoding="utf-8") as f:
        f.write("""<!DOCTYPE html>
    <html>

    <head>
        <meta charset="utf-8">
        <title>豆瓣250打卡</title>
        <style>
            .flex-container {
                display: -webkit-flex;
                display: flex;
                -webkit-justify-content: center;
                justify-content: center;
                min-height:100px;
                width: 100%;
                background-color: #fefdca;
            }

            .flex-item {
                border-radius: 10px;
                background-color: #a5dee5;
                width: 8%;
                margin: 10px;
            }

            .introduce {
                padding-top: 2rem;
                height: 10rem;
                background-color: #fefdca;
            }

            .box1::after {
                content: " ";
                position: absolute;
                background: #dcf7ad;
                width: 18px;
                height: 18px;
                left: 12px;
            }

            .box2::after {
                content: " ";
                position: absolute;
                margin-top: 5px;
                background: #ffcfdf;
                width: 17px;
                height: 17px;
                left: 12px;
            }

            .box3::after {
                content: " ";
                margin-top: 5px;
                position: absolute;
                background: #a5dee5;
                width: 17px;
                height: 17px;
                left: 12px;
            }

            .color-intro {
                width: 10rem;
                height: 10rem;
                border-radius: 10px;
                text-align: left;
                position: absolute;
                right: 3rem;
                top: 3rem;
            }

            .color1 {
                background-color: #e0f9b5;
            }

            .color0 {
                background-color: #ffcfdf;
            }

            .color2 {
                background-color: #a5dee5;
            }

            p, h1 {
                text-align: center;
            }
            .flex-item a {
                margin-top: .5rem;
                display:block;
                color: #000;
                font-weight: bold;
                font-size: 1.4rem;
                font-family: 'SimSun', Courier, monospace;
                text-decoration: none;
            }
        </style>
        <link href="https://cdn.bootcdn.net/ajax/libs/twitter-bootstrap/5.0.2/css/bootstrap.min.css" rel="stylesheet">
    </head>

    <body>
        <div class="introduce">
            <h1>公告</h1>
            <p>这是一个豆瓣250刷电影的页面。欢迎访问啊</p>
            <div class="color-intro">
                <p class="box1">表示看过</p>
                <p class="box2">表示没看过</p>
                <p class="box3">表示不太清楚</p>
            </div>
        </div>""")
        for i in range(25):
            f.write("<div class=\"flex-container\">")
            for j in range(1, 11):
                idx = i*10 + j
                res = 0
                if df.loc[idx,"title"] in d:
                    res = d[df.loc[idx,"title"]]

                f.write("<div class=\"flex-item color{}\">{:03d}<a href=\"{}\" data-bs-toggle='tooltip' data-bs-placement='top' title='{}' target=\"_blank\">《{}》</a></div>".format(res,idx,df.loc[idx,"link"],df.loc[idx,"judge"],df.loc[idx,"title"]))

            f.write("</div>")

        f.write("""	<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.10.2/dist/umd/popper.min.js"></script>
        <script src="https://cdn.bootcdn.net/ajax/libs/twitter-bootstrap/5.0.2/js/bootstrap.min.js"></script>
        <script>
            var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
            var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
                return new bootstrap.Tooltip(tooltipTriggerEl)
            })
        </script>
    </body>

    </html>""")