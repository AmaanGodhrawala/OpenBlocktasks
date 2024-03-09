from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:MySQL@localhost:3306/openblockschema'
db = SQLAlchemy(app)
class Dataset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.TIMESTAMP)
    wallet_address = db.Column(db.String(255))
    point_value = db.Column(db.Float)
    year = db.Column(db.Integer)
    month = db.Column(db.Integer)
    day = db.Column(db.Integer)
@app.route('/api/dataset', methods=['GET'])
def get_dataset():
    wallet_address = request.args.get('wallet_address')
    from_date = request.args.get('from_date')
    to_date = request.args.get('to_date')

    result = db.session.query(
        Dataset.wallet_address,
        Dataset.year,
        Dataset.month,
        Dataset.day,
        db.func.sum(Dataset.point_value).label('total_points')
    ).filter(
        Dataset.wallet_address == wallet_address,
        Dataset.date >= from_date,
        Dataset.date <= to_date
    ).group_by(
        Dataset.wallet_address,
        Dataset.year,
        Dataset.month,
        Dataset.day
    ).all()

    response_data = [{
        'wallet_address': row.wallet_address,
        'from_date': from_date,
        'to_date': to_date,
        'total_points': row.total_points
    } for row in result]

    sum_of_points = 0

    for i in range(len(response_data)):
        sum_of_points += response_data[i]['total_points']
    
    response_data = [
        {
        'wallet_address': wallet_address,
        'from_date': from_date,
        'to_date': to_date,
        'total_points': sum_of_points
    }
    ]


    return jsonify(response_data)
if __name__ == "__main__":
    app.run(debug=True)
