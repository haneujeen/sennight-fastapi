//
//  ActivitiesCardView.swift
//  Sennight
//
//  Created by 한유진 on 6/27/24.
//

import SwiftUI

struct ActivitiesCardView: View {
    var body: some View {
        Section(header: Text("Activities")) {
            ForEach(0..<3) { _ in
                ActivityRowView()
            }
        }
    }
}

#Preview {
    ActivitiesCardView()
}
