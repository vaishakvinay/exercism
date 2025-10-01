//
// This is only a SKELETON file for the 'House' exercise. It's been provided as a
// convenience to get you started writing code faster.
//
export class House {
  static parts = [
    'the house that Jack built.',
    'the malt',
    'the rat',
    'the cat',
    'the dog',
    'the cow with the crumpled horn',
    'the maiden all forlorn',
    'the man all tattered and torn',
    'the priest all shaven and shorn',
    'the rooster that crowed in the morn',
    'the farmer sowing his corn',
    'the horse and the hound and the horn'
  ];

  static actions = [
    'lay in',
    'ate',
    'killed',
    'worried',
    'tossed',
    'milked',
    'kissed',
    'married',
    'woke',
    'kept',
    'belonged to'
  ];

  static verse(n) {
    const lines = [];
    lines.push(`This is ${House.parts[n - 1]}`);
    
    for (let i = n - 1; i > 0; i--) {
      lines.push(`that ${House.actions[i - 1]} ${House.parts[i - 1]}`);
    }
    return lines;
  }
  

  

static verses(start, end) {
  const result = [];
  for (let i = start; i <= end; i++) {
    result.push(...House.verse(i)); // add all lines of verse i
    if (i < end) result.push('');   // add blank line except after last verse
  }
  return result;
}
}

