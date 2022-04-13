from datetime import datetime
from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from psycopg2 import Time
from myapp import db 
from myapp.models import TimeCard
from myapp.time_cards.forms import TimeCardForm

time_cards = Blueprint('time_cards', __name__)

@time_cards.route('/create', methods=['GET', 'POST'])
@login_required
def create_card():
  form = TimeCardForm()
  if form.validate_on_submit():
    time_card = TimeCard(user_id=current_user.id)
    db.session.add(time_card)
    db.session.commit()
    flash('Time Card Created')
    print('Time card was created')
    return redirect(url_for('core.index'))
  return render_template('punch_in.html', form=form)

@time_cards.route('/<int:time_card_id>/update',methods=['GET','POST'])
@login_required
def update(time_card_id):
  time_card = TimeCard.query.get_or_404(time_card_id)

  if time_card.employee != current_user:
        abort(403)

  form = TimeCardForm()

  if form.validate_on_submit():
        time_card.time_out = datetime.now()
        db.session.commit()
        flash('Time Card Updated')
        return redirect(url_for('core.index'))

  return render_template('punch_in.html',title='Updating',form=form)