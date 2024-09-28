function solution(begin, target, words) {
  let min = bfs(begin, target, words);
  return min;
}

function bfs(begin, target, words) {
  const queue = [[begin, 0]];
  const visited = Array.from({ length: words.length }, () => false);
  let idx = 0;

  while (queue.length !== idx) {
    const pos = queue[idx++];
    let [currentWord, level] = pos;

    if (currentWord === target) {
      return level;
    }

    words.forEach((targetWord, index) => {
      if (isVisitEnable(currentWord, targetWord) && !visited[index]) {
        visited[index] = true;
        queue.push([targetWord, level + 1]);
      }
    });
  }

  return 0;
}

function isVisitEnable(currentWord, targetWord) {
  let diff = 0;

  currentWord.split("").forEach((char, index) => {
    if (targetWord[index] !== char) diff++;
  });

  return diff === 1 ? true : false;
}