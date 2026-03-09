from flask import Blueprint, render_template, request, redirect
from database.db import get_connection

transaction_bp = Blueprint("transaction", __name__)


@transaction_bp.route("/")
def home():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM transactions")
    transactions = cursor.fetchall()

    conn.close()
    return render_template("index.html", transactions=transactions)

@transaction_bp.route("/set_budget",methods=["GET","POST"])
def set_budget():

    conn = get_connection()
    cursor = conn.cursor()

    if request.method == "POST":
        limit = request.form["limit"]

        cursor.execute("DELETE FROM budget")
        cursor.execute("INSERT INTO budget (monthly_limit) VALUES (?)",(limit,))

        conn.commit()
        conn.close()

        return redirect("/")
    conn.close()