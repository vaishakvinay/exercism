//
// This is only a SKELETON file for the 'Twelve Days' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

let gifts = [
  'a Partridge in a Pear Tree.',
  'two Turtle Doves',
  'three French Hens',
  'four Calling Birds',
  'five Gold Rings',
  'six Geese-a-Laying',
  'seven Swans-a-Swimming',
  'eight Maids-a-Milking',
  'nine Ladies Dancing',
  'ten Lords-a-Leaping',
  'eleven Pipers Piping',
  'twelve Drummers Drumming',
];

let days = [
  'first',
  'second',
  'third',
  'fourth',
  'fifth',
  'sixth',
  'seventh',
  'eighth',
  'ninth',
  'tenth',
  'eleventh',
  'twelfth',
];

export function recite(startVerse, endVerse = startVerse) {
  let result = [];

  for (let i = startVerse; i <= endVerse; i++) {
    let line = `On the ${days[i - 1]} day of Christmas my true love gave to me: `;

    let dailyGifts = [];
    for (let j = i - 1; j >= 0; j--) {
      if (j == 0 && i > 1) {
        dailyGifts.push('and ' + gifts[0]);  // fixed missing space + variable typo
      } else {
        dailyGifts.push(gifts[j]);
      }
    }

    line += dailyGifts.join(', ') + '\n';
    result.push(line);
  }

  if (endVerse === startVerse) {
    return result[0];
  } else {
    return result.join('\n');
  }
}


         

