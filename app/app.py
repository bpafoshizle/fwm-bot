def main():
    import logging
    import os

    from dotenv import load_dotenv

    # Set the logging level based on the environment variable.
    log_level = os.environ.get("LOGLEVEL", "INFO")
    log_level = log_level.upper()

    if log_level not in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
        raise ValueError(
            "Invalid log level. Must be one of: DEBUG, INFO, WARNING, ERROR, CRITICAL"
        )

    logging.basicConfig(
        format="%(asctime)s %(levelname)-4s %(name)-25s %(message)s",
        level=logging.INFO,
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    load_dotenv(override=True)

    from pydiscogs import botbuilder

    bot = botbuilder.build_bot("fwm-bot.yaml")
    logging.info("running bot: %s", bot)
    bot.run(bot.discord_token)


if __name__ == "__main__":
    main()
