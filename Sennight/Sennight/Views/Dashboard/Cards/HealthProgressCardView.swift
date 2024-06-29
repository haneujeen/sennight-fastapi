//
//  HealthProgressCardView.swift
//  Sennight
//
//  Created by 한유진 on 6/27/24.
//

import SwiftUI

struct HealthProgressCardView: View {
    var body: some View {
        Section {
            HStack {
                Spacer()
                VStack {
                    Text("Health progress card")
                    Spacer()
                    CircularGauge(progress: 0.75)
                    Spacer()
                    Button("Add smoking") {
                        print("Smoking added...")
                    }
                }
                Spacer()
            }
        }
    }
}

#Preview {
    HealthProgressCardView()
}
