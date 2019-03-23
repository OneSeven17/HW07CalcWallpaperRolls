from flask import Flask, render_template, request

from calc_rolls import calculate_roll_quantity


def main():
    app = Flask(__name__)


    @app.route('/')
    def fronpage():
        room_length = request.args.get('room_length')
        room_width = request.args.get('room_width')
        room_height = request.args.get('room_height')
        roll_width = request.args.get('roll_width')
        roll_length = request.args.get('roll_length')

        if room_length and room_width and room_height and roll_width and roll_length:
            roll_quantity = calculate_roll_quantity(int(room_length), int(room_width), int(room_height), int(roll_width), int(roll_length))
            return render_template('index.html', title='Roll quantity', roll_quantity=roll_quantity, room_length=room_length, room_width=room_width, room_height=room_height, roll_width=roll_width, roll_length=roll_length)
        return render_template('index.html', title='Roll quantity')


    app.run(port=9873, debug=True)


if __name__ == '__main__':
    main()