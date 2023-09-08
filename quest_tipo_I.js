// ingresamos un número y lo guardamos en la variable 'num'
let num = window.prompt("Ingresa un número:");

// Comienza un bucle 'for' que se ejecutará 10 veces, una vez para cada valor de 'i' desde 1 hasta 10
for (let i = 1; i <= 10; i++) {
    // Muestra en la consola la multiplicación de 'num' por 'i'
    console.log(num, "*", i, "=", num * i);
}
