from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def run_main():
    try:
        # Run the main.py script
        result = subprocess.run(['python', 'main.py'], capture_output=True, text=True)
        
        # Return the output of the main.py script
        return jsonify({
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode
        })
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
