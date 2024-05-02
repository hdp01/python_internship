import tornado.ioloop
import tornado.web

class CalculatorHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("static/calculator.html")

    def post(self):
        num1 = float(self.get_argument("num1"))
        num2 = float(self.get_argument("num2"))
        operator = self.get_argument("operator")

        result = None
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error: Division by zero!"

        self.render("static/result.html", result=result)

def make_app():
    return tornado.web.Application([
        (r"/", CalculatorHandler),
        (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": "static"}),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("Listening on http://localhost:8888")
    tornado.ioloop.IOLoop.current().start()
