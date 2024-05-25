from flask import Flask, render_template

from core.commons import Error


def init_error_views(app: Flask):

    @app.errorhandler(404)
    def page_not_found_error_page_view(_):
        return render_template(
            "pages/error/index.html", status_code=404, message="Página não encontrada."
        )

    @app.errorhandler(Exception)
    @app.errorhandler(Error)
    @app.errorhandler(500)
    def internal_server_error_page_view(error):
        print("error", error, flush=True)
        return render_template(
            "pages/error/index.html",
            status_code=500,
            message="Erro interno no servidor.",
            internal_message=error,
        )
