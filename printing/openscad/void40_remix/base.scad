// Refactor bottom for itsy-bitsy
// Update wider board and deeper fitting 
module itsy_bitsy() {
    union() {
        color([1,0,0])
        translate([5, 30, 0])
        cube([7, 5, 4]);
        color([0,1,0])
        cube([17.2, 35, 2]);
    }
}

difference() {
    union() {
        import("../../base_boards/void40/files/VOID40OP_-_Bottom.stl", convexity=3);
        rotate([5, 0, 0])
        translate([20, -23.9, 4])
        cube([40, 4, 10]);
    }
    
    translate([20, -65, .2])
    cube([40, 35, 10]);

    translate([30.4, -31.2, 4])    
    union() {
    color([0,0,1])
        translate([2.48,5.1,1.7])
        cube([12, 12, 4]);
    color([1,0,1])
        cube([17.4, 10, 2.2]);
    }
}

translate([33.6, -60.2, .2])
color([1, 1, 1])
union() {
    translate([1.8,0,0])
    cube([6, 3, 5.5]);
    cube([10, 7, 3.8]);
}

// translate([30.5, -57.1, 4.2])
// itsy_bitsy();