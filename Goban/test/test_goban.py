import goban


def test_GoBoard_initialize():
    # Get the options for the chosen size
    options = goban.sizeOptions['19']

    # Enrich options with defaults
    options.update(goban.DefaultOptions)

    return goban.GoBoard(options)


def test_GoBoard_draw():
    board = test_GoBoard_initialize()

    board.draw()
