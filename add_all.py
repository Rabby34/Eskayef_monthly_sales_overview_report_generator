from PIL import Image, ImageDraw, ImageFont, ImageFilter

back = Image.open("background.png")
banner = Image.open("tcpl_banner.png")
kpi1 = Image.open("1st_kpi.png")
kpi2 = Image.open("2nd_kpi.png")
kpi3 = Image.open("3rd_kpi.png")
kpi4 = Image.open("4th_kpi.png")
kpi5 = Image.open("5th_kpi.png")
kpi6 = Image.open("6th_kpi.png")
kpi7 = Image.open("7th_kpi.png")
kpi8 = Image.open("8th_kpi.png")
kpi9 = Image.open("9th_kpi.png")

cumulative_t_s = Image.open("cumulative_with_value.png")
changed_extra_space_mid = Image.open("changed_extra_space_mid.png")

extra_background = Image.open("extra_background.png")
top5_brand = Image.open("changed_top5_brand_info.png")
top5_brand_contribution = Image.open("contribution_pic.png")

top5_brand_return = Image.open("return_bar_with_value.png")
top10_chemist_return = Image.open("chemist_bar_with_value.png")

top9_nsm = Image.open("top9_customer_info.png")
outstanding_pie = Image.open("outstanding_donut.png")

aging_days = Image.open("aging_outstanding.png")
# left_mirror = Image.open("left_mirror2.png")
# right_mirror = Image.open("right_mirror2.png")

# mid_pie = Image.open("mid_pie.png")

imageSize = Image.new('RGB', (1270,3180 ))#2110
imageSize.paste(back, (0, 0))
imageSize.paste(banner, (10, 10))

imageSize.paste(kpi7, (10, 265))#target
imageSize.paste(kpi9, (430, 265))
imageSize.paste(kpi1, (850, 265))

imageSize.paste(kpi6, (10, 440))
imageSize.paste(kpi2, (430, 440))
imageSize.paste(kpi3, (850, 440))

imageSize.paste(kpi4, (10, 615))
imageSize.paste(kpi5, (430, 615))
imageSize.paste(kpi8, (850, 615))

imageSize.paste(changed_extra_space_mid, (0, 790))
imageSize.paste(cumulative_t_s, (-40, 855))

imageSize.paste(cumulative_t_s, (-40, 855))

imageSize.paste(extra_background, (0, 1500))
imageSize.paste(top5_brand, (0, 1300))
imageSize.paste(top5_brand_contribution, (880, 1315))

imageSize.paste(top5_brand_return, (120, 1690))
imageSize.paste(top10_chemist_return, (755, 1690))

imageSize.paste(top9_nsm, (0, 2320))

imageSize.paste(outstanding_pie, (0, 2700))
imageSize.paste(aging_days, (750, 2750))
# imageSize.paste(left_mirror, (0, 890))
# imageSize.paste(right_mirror, (430, 890))#290,870
#
# imageSize.paste(mid_pie, (770, 890))

imageSize.save("./marge_all1.png")

print("all are merged together.")
