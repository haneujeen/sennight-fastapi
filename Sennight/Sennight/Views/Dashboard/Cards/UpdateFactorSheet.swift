//
//  UpdateFactorSheet.swift
//  Sennight
//
//  Created by 한유진 on 6/28/24.
//

import SwiftUI

struct UpdateFactorSheet: View {
    @Binding var isPresentingUpdateFactorSheet: Bool
    
    var body: some View {
        Text("Update factor sheet")
    }
}

#Preview {
    UpdateFactorSheet(isPresentingUpdateFactorSheet: .constant(true))
}
