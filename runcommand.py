import web
import os

class CommandExecution:
    def GET(self):
        return """
            <form method="POST" action="/execute">
                <input type="text" name="command" />
                <input type="submit" value="Execute" />
            </form>
        """

class ExecuteCommand:
    def POST(self):
        data = web.input()
        command = data.command

        try:
            os.system(command)
            return web.seeother('/')

        except Exception as e:
            return "Error: " + str(e)

urls = (
    '/', 'CommandExecution',
    '/execute', 'ExecuteCommand'
)

app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()
