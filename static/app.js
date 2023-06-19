class Boggle {
  constructor(board, time = 60) {
    this.board = $("#" + board);
    this.words = new Set();
    this.score = 0;
    this.time = time;
    this.showTimer();

    this.timer = setInterval(this.timeLeft.bind(this), 1000);

    $(".boggle-form", this.board).on("submit", this.handleRequests.bind(this));
  }

  showMsg(msg) {
    $(".msg", this.board).text(msg);
  }

  showScore() {
    $(".score", this.board).text(this.score);
  }

  async handleRequests(evt) {
    evt.preventDefault();
    let $guess = $("#guess", this.board);
    let word = $guess.val();
    let len = word.length;
    let $score = $(".score", this.board);

    if (this.words.has(word)) {
      this.showMsg("This word has already been entered before.");
      $guess.val("");
      return;
    }

    let response = await axios.get("/submit-guess", {
      params: { word: word },
    });
    let result = response.data["result"];

    if (result === "not-word") {
      this.showMsg("Invalid entry. Please enter a valid word.");
    } else if (result === "not-on-board") {
      this.showMsg("Unfortunately, that word is not part of the available choices.");
    } else if (result === "ok") {
      this.showMsg("Valid entry!");
      this.words.add(word);
      this.score += len;
      this.showScore();
    }

    $guess.val("");
  }
  showTimer() {
    $(".timer", this.board).text(this.time);
  }

  timeLeft() {
    this.time -= 1;
    this.showTimer();

    if (this.time === 0) {
      clearInterval(this.timer);
      this.score = 0;
      this.showScore();
      $(".boggle-form input").prop("disabled", true);
      $(".msg", this.board).text("Time's up! No more guesses allowed.");
    }
  }
}
