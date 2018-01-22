var TennisGame1 = function(player1Name, player2Name) {
  this.mScore1 = 0;
  this.mScore2 = 0;
  this.player1Name = player1Name;
  this.player2Name = player2Name;

  this.wonPoint = (playerName) => {
    if (playerName === "player1") this.mScore1 += 1;
    else this.mScore2 += 1;       
  };

  this.getScore = () => {
    let score = "";
    let tempScore = 0;
    if (this.mScore1 === this.mScore2) {
      if (this.mScore1 === 0) score = 'Love-All';
      else if (this.mScore1 === 1) score = "Fifteen-All";
      else if (this.mScore1 === 2) score = "Thirty-All";
      else score = "Deuce";

    } else if (this.mScore1 >= 4 || this.mScore2 >= 4) {
      let minusResult = this.mScore1 - this.mScore2;
      if (minusResult === 1) score = "Advantage player1";
      else if (minusResult === -1) score = "Advantage player2";
      else if (minusResult >= 2) score = "Win for player1";
      else score = "Win for player2";
      
    } else {
      for (let i = 1; i < 3; i++) {
        if (i === 1) tempScore = this.mScore1;
        else {
          score += "-";
          tempScore = this.mScore2;
        }
        if (tempScore === 0) score += "Love";
        else if (tempScore === 1) score += "Fifteen";
        else if (tempScore === 2) score += "Thirty";
        else if (tempScore === 3) score += "Forty";
      }
    }
    return score;
  };
};

if (typeof window === "undefined") {
  module.exports = TennisGame1;
}