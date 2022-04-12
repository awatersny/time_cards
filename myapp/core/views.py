from flask import render_template, request, Blueprint
from myapp.models import TimeCard

core = Blueprint('core', __name__)

@core.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    # BlogPost.query.order_by(BlogPost.date.desc()).paginate(page=page, per_page=5)
    time_cards = TimeCard.query.order_by(TimeCard.time_in.desc()).paginate(page=page, per_page=5)
    return render_template('index.html', time_cards=time_cards)

@core.route('/info')
def info():
    return render_template('info.html')