import Foundation
import Vision
import CoreImage
import AppKit

let args = CommandLine.arguments
guard args.count >= 3 else { print("uso: segbin <dir_frames> <dir_masks>"); exit(1) }
let inDir = args[1], outDir = args[2]
try? FileManager.default.createDirectory(atPath: outDir, withIntermediateDirectories: true)
let files = (try! FileManager.default.contentsOfDirectory(atPath: inDir)).filter { $0.hasSuffix(".png") }.sorted()
let ctx = CIContext(options: [.useSoftwareRenderer: false])

for (i, f) in files.enumerated() {
    let url = URL(fileURLWithPath: inDir + "/" + f)
    guard let img = CIImage(contentsOf: url) else { print("ERR \(f)"); continue }
    let req = VNGeneratePersonSegmentationRequest()
    req.qualityLevel = .accurate
    req.outputPixelFormat = kCVPixelFormatType_OneComponent8
    let handler = VNImageRequestHandler(ciImage: img, options: [:])
    do { try handler.perform([req]) } catch { print("ERR perform \(f)"); continue }
    guard let obs = req.results?.first as? VNPixelBufferObservation else { print("ERR nores \(f)"); continue }
    var mask = CIImage(cvPixelBuffer: obs.pixelBuffer)
    let sx = img.extent.width / mask.extent.width
    let sy = img.extent.height / mask.extent.height
    mask = mask.transformed(by: CGAffineTransform(scaleX: sx, y: sy))
    let rep = NSBitmapImageRep(ciImage: mask)
    if let data = rep.representation(using: .png, properties: [:]) {
        try? data.write(to: URL(fileURLWithPath: outDir + "/" + f))
    }
    if i % 100 == 0 { print("\(i)/\(files.count)"); fflush(stdout) }
}
print("LISTO \(files.count)")
