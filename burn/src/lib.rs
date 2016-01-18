use std::thread;

#[no_mangle]
pub extern fn triple(x: i32) -> i32 {

    let handles: Vec<_> = (0..10).map(|i| {
        thread::spawn(move || {
            println!("Thread {} running", i);

            let mut x = 0;
            while x < 1_000_000_000 {
                x += 1
            }

            println!("Thread {} returning", i);
        })
    }).collect();

    for h in handles {
        h.join().unwrap();
    }

    x * 3
}

#[test]
fn it_works() {
    assert!(triple(3) == 9);
}
