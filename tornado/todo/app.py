import tornado.ioloop
import tornado.web
import pymysql.cursors

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    database='tornado_todo',
    cursorclass=pymysql.cursors.DictCursor
)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        with connection.cursor() as cursor:
            sql = "SELECT * FROM tasks"
            cursor.execute(sql)
            tasks = cursor.fetchall()

        self.render("templates/index.html", tasks=tasks)

    def post(self):
        task = self.get_argument("task")
        action = self.get_argument("action")

        if action == "add":
            with connection.cursor() as cursor:
                sql = "INSERT INTO tasks (task) VALUES (%s)"
                cursor.execute(sql, (task,))
                connection.commit()

        elif action == "update":
            task_id = self.get_argument("id")
            with connection.cursor() as cursor:
                sql = "UPDATE tasks SET task=%s WHERE id=%s"
                cursor.execute(sql, (task, task_id))
                connection.commit()

        elif action == "delete":
            task_id = self.get_argument("id")
            with connection.cursor() as cursor:
                sql = "DELETE FROM tasks WHERE id=%s"
                cursor.execute(sql, (task_id,))
                connection.commit()

        self.redirect("/")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("Listening on http://localhost:8888")
    tornado.ioloop.IOLoop.current().start()
