from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    name = request.args.get("name")

    if not name:
        return """
        <h2>Welcome to Flask App 🚀</h2>
        <p>Please enter your name in the URL like this:</p>
        <p><b>?name=yourname</b></p>
        """

    upper_name = name.upper()
    reversed_name = name[::-1]
    length = len(name)

    return f"""
    <html>
        <head>
            <title>Flask Assignment</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f4f6f8;
                    text-align: center;
                    padding-top: 50px;
                }}
                .card {{
                    background: white;
                    width: 400px;
                    margin: auto;
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0 0 10px rgba(0,0,0,0.1);
                }}
            </style>
        </head>
        <body>
            <div class="card">
                <h1>Hello {upper_name} 👋</h1>
                <p><b>Uppercase:</b> {upper_name}</p>
                <p><b>Reversed Name:</b> {reversed_name}</p>
                <p><b>Character Count:</b> {length}</p>
            </div>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
