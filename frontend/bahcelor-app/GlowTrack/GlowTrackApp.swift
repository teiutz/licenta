//  GlowTrackApp.swift
//  GlowTrack
//  Created by Tea Tatoiu on 02.04.2025.

import SwiftUI

@main
struct GlowTrackApp: App {
    let persistenceController = PersistenceController.shared

    var body: some Scene {
        WindowGroup {
            ContentView()
                .environment(\.managedObjectContext, persistenceController.container.viewContext)
        }
    }
}
