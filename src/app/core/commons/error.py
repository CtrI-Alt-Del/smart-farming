from cowsay import func as cow_say


class Error(Exception):
    def __init__(
        self,
        ui_message="Pultz, algo deu errado",
        internal_message="Internal Server Error",
    ):
        self.ui_message = ui_message
        self.internal_message = internal_message

        cow_say(internal_message)
