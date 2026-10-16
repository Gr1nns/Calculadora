use std::io;
fn main(){
    let mut alim = String::new();
    let mut blim = String::new();
    let mut clim = String::new();
    let mut see = String::new();
    println!("Wich operation do you want to do? Adition(A), Subtraction(S), Division(D) or Multiplication(M) ");
    io::stdin()
        .read_line(&mut clim)
        .expect("Error");
    println!("Type the first number: ");
    io::stdin()
        .read_line(&mut alim)
        .expect("Error");
    println!("Type the second number: ");
    io::stdin()
        .read_line(&mut blim)
        .expect("Error");

    let a: f64 = alim.trim().parse().expect("Invalid first number");
    let b: f64 = blim.trim().parse().expect("Invalid second number");

    match clim.trim(){
        "A"|"a"=>println!("The value of the answer is: {}", a + b),
        "S"|"s"=>println!("The value of the answer is: {}",a-b),
        "D"|"d"=>{
            if b == 0.0{
                println!("Cannot divide by zero");
            }else{
                println!("The value of the answer is: {}",a/b);
            }
        }
        "M"|"m"=>println!("The value of the answer is: {}",a*b),
        _ => println!("Error: unknow opperation"),
    }
 io::stdin().read_line(&mut see).expect("Error");
}
