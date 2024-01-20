from app import App

application = App()

try:

    application.run()

except Exception as e:

    application.model.log.debug(
        "Error: " +
        type(e).__name__ + ": " +
        e.__str__()
    )
