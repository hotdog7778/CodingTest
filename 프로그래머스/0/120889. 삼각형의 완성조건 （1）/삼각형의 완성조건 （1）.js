function solution(sides) {
    const numbers = sides
    
    numbers.sort((a, b) => b - a);
    
    if(numbers[0] < numbers[1]+numbers[2]) {
        return 1;
    }
    
    return 2;
    
}