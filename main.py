# from flask import Flask, render_template, jsonify, request
# from flask_pymongo import PyMongo
# import openai
# import os
# from dotenv import load_dotenv

# load_dotenv()

#  openai.api_key = os.getenv("OPENAI_API_KEY")       
#  mongo_uri = os.getenv("MONGO_URI")  

# app = Flask(__name__)
# app.config["MONGO_URI"] = mongo_uri
# mongo = PyMongo(app)

# @app.route("/")
# def home():
#     chats = list(mongo.db.chats.find({}, {"_id": 0})) 
#     return render_template("index.html", myChats=chats)

# @app.route("/api", methods=["POST"])
# def qa():
#     data = request.get_json()
#     if not data or "question" not in data:
#         return jsonify({"error": "Invalid request"}), 400

#     question = data["question"]
#     chat = mongo.db.chats.find_one({"question": question}, {"_id": 0})

#     if chat:
#         return jsonify(chat)

#     response = openai.Completion.create(
#         model="text-davinci-003",
#         prompt=question,
#         temperature=0.7,
#         max_tokens=256,
#         top_p=1,
#         frequency_penalty=0,
#         presence_penalty=0
#     )

#     answer = response["choices"][0]["text"].strip()
#     mongo.db.chats.insert_one({"question": question, "answer": answer})

#     return jsonify({"question": question, "answer": answer})

# if __name__ == "__main__":
#     app.run(debug=True, port=5001)
