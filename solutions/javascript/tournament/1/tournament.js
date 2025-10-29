//
// This is only a SKELETON file for the 'Tournament' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const tournamentTally = (input) => {
    let tableHeader = 'Team                           | MP |  W |  D |  L |  P'
  if (!input || !input.trim())return tableHeader;
  
const matches = input.trim().split('\n');
 const scores = {};
  function initTeam(team) {
  if (!scores[team]) {
    scores[team] = { MP: 0, W: 0, D: 0, L: 0, P: 0 };
  }
}

for (const match of matches) {
  const [team1, team2, result] = match.split(';');
  
    initTeam(team1);
    initTeam(team2);
  scores[team1].MP++;
    scores[team2].MP++;

    if (result === 'win') {
      scores[team1].W++;
      scores[team1].P += 3;
      scores[team2].L++;
    } else if (result === 'loss') {
      scores[team2].W++;
      scores[team2].P += 3;
      scores[team1].L++;
    } else if (result === 'draw') {
      scores[team1].D++;
      scores[team2].D++;
      scores[team1].P++;
      scores[team2].P++;
    }
  }
  const sortedTeams = Object.keys(scores).sort((a, b) => {
    if (scores[b].P !== scores[a].P) return scores[b].P - scores[a].P;
    return a.localeCompare(b);
  });

const tableRows = sortedTeams.map(team => {
  const { MP, W, D, L, P } = scores[team];
  return `${team.padEnd(31)}| ${String(MP).padStart(2)} | ${String(W).padStart(2)} | ${String(D).padStart(2)} | ${String(L).padStart(2)} | ${String(P).padStart(2)}`;
});


  return [tableHeader, ...tableRows].join('\n');
};
