function somar() {
    let num1 = parseFloat(document.getElementById("num1").value);
    let num2 = parseFloat(document.getElementById("num2").value);
    let resultado = num1 + num2;
    document.getElementById("resultado").innerHTML = "Resultado: " + resultado;
}
function subtrair() {
    let num1 = parseFloat(document.getElementById("num1").value);
    let num2 = parseFloat(document.getElementById("num2").value);
    let resultado = num1 - num2;
    document.getElementById("resultado").innerHTML = "Resultado: " + resultado;
}
function dividir() {
    let num1 = parseFloat(document.getElementById("num1").value);
    let num2 = parseFloat(document.getElementById("num2").value);
    let resultado = num1 / num2;
    
    if (num2 == 0) {
        document.getElementById("resultado").innerHTML = "impossível dividir por 0"
    } else {
        document.getElementById("resultado").innerHTML = "Resultado: " + resultado;
    }
}
function multiplicar() {
    let num1 = parseFloat(document.getElementById("num1").value);
    let num2 = parseFloat(document.getElementById("num2").value);
    let resultado = num1 * num2;
    document.getElementById("resultado").innerHTML = "Resultado: " + resultado;
}