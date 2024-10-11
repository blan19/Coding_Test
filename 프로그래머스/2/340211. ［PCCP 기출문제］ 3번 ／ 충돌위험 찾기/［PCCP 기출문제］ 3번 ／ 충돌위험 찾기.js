function solution(points, routes) {
    const pointMap = new Map(points.map((point, index) => [index + 1, point]));
    
    function getPos(current, target) {
        if (current[0] < target[0]) return [current[0] + 1, current[1]];
        if (current[0] > target[0]) return [current[0] - 1, current[1]];
        if (current[1] < target[1]) return [current[0], current[1] + 1];
        if (current[1] > target[1]) return [current[0], current[1] - 1];
        return current;
    }
    
    function simulate(route) {
        let positions = [];
        let current = pointMap.get(route[0]);
        for (let i = 1; i < route.length; i++) {
            let target = pointMap.get(route[i]);
            while (current[0] !== target[0] || current[1] !== target[1]) {
                positions.push(current.join(','));
                current = getPos(current, target);
            }
        }
        positions.push(current.join(','));
        return positions;
    }
    
    let robotPositions = routes.map(simulate);
    let maxTime = Math.max(...robotPositions.map(p => p.length));
    
    let dangerCount = 0;
    for (let t = 0; t < maxTime; t++) {
        let positionCount = new Map();
        for (let robot = 0; robot < robotPositions.length; robot++) {
            if (t < robotPositions[robot].length) {
                let pos = robotPositions[robot][t];
                positionCount.set(pos, (positionCount.get(pos) || 0) + 1);
            }
        }
        for (let count of positionCount.values()) {
            if (count > 1) dangerCount++;
        }
    }
    
    return dangerCount;
}