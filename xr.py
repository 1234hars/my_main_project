import qrcode
img = qrcode.make('Some data here')
type(img)  # qrcode.image.pil.PilImage
img.save("some_file.png")



import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('Some data')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")


img = qr.make_image(back_color=(255, 195, 235), fill_color=(55, 95, 35))


import qrcode
import qrcode.image.svg

if method == 'basic':
    # Simple factory, just a set of rects.
    factory = qrcode.image.svg.SvgImage
elif method == 'fragment':
    # Fragment factory (also just a set of rects)
    factory = qrcode.image.svg.SvgFragmentImage
else:
    # Combined path factory, fixes white space that may occur when zooming
    factory = qrcode.image.svg.SvgPathImage

img = qrcode.make('Some data here', image_factory=factory)


qrcode.image.svg.SvgFillImage
qrcode.image.svg.SvgPathFillImage


import qrcode
qr = qrcode.QRCode(image_factory=qrcode.image.svg.SvgPathImage)
qr.add_data('Some data')
qr.make(fit=True)

img = qr.make_image(attrib={'class': 'some-css-class'})



img.to_string(encoding='unicode')



import qrcode
from qrcode.image.pure import PyPNGImage
img = qrcode.make('Some data here', image_factory=PyPNGImage)



import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
qr.add_data('Some data')

img_1 = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())
img_2 = qr.make_image(image_factory=StyledPilImage, color_mask=RadialGradiantColorMask())
img_3 = qr.make_image(image_factory=StyledPilImage, embeded_image_path="/path/to/image.png")



import io
import qrcode
qr = qrcode.QRCode()
qr.add_data("Some text")
f = io.StringIO()
qr.print_ascii(out=f)
f.seek(0)
print(f.read())




import qrcode
qr = qrcode.QRCode()
qr.add_data('Some data')
img = qr.make_image()
qr.clear()
qr.add_data('New data')
other_img = qr.make_image()





