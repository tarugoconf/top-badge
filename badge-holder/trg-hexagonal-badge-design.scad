module trg_hexagonal_badge() {
    // TRG Badge Dimensions
    //   [26.25, 45.46]        [134.25, 45.46]           
    //          ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬                        
    //         ▬                 ▬                       
    //        ▬                   ▬                      
    //       ▬                     ▬                     
    //      ▬                       ▬                    
    //     ▬  [0, 0]      [160.5, 0] ▬                   
    //      ▬                       ▬                    
    //       ▬                     ▬                     
    //        ▬                   ▬                      
    //         ▬                 ▬                       
    //          ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬                        
    // [26.25, -45.46]            [134.25, -45.46]       
    //

    polygon(
        points=[
            [0, 0],
            [26.25, -45.46],
            [134.25, -45.46],
            [160.50, 0],
            [134.25, 45.46],
            [26.25, 45.46]
        ],
        paths=[
            [0, 1, 2, 3, 4, 5] // Ordered points to form the hexagon
        ]
    );
}

module circle_hole_for_lanyard() {
    translate([160.50-6, 0]) // Position the hole
    circle(r=2.5); // Hole radius
}

module trg_hexagonal_badge_with_lanyard_hole() {
    difference() { // Subtract the circle hole from the hexagon
        trg_hexagonal_badge();
        circle_hole_for_lanyard();
    }
}


module trg_hexagonal_badge_with_lanyard_hole_extruded() {
    linear_extrude(height=1.2) { // Extrude the badge to a height of 1.2mm
        trg_hexagonal_badge_with_lanyard_hole();
    }
}
