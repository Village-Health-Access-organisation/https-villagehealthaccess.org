"""Page content for the Village Health Access site.

Content is taken from the previous villagehealthaccess.org. Goals are labelled as goals,
never as results. <span class="ph">...</span> marks a fact still to be confirmed or supplied.
"""

# Official logo (Nov 2026), traced from Donald's Illustrator file. Full files in src/static/brand/.
LOGO = '<svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="336.7 525.6 228.8 228.8"><path fill="#0b6b45" d="M 513.55 642.75 L 478.41 642.75 C 478.50 645.53 478.57 648.34 478.57 651.20 C 478.57 696.76 466.16 733.69 450.85 733.69 C 438.01 733.69 427.21 707.66 424.07 672.36 L 386.23 672.36 C 388.97 717.18 416.85 752.41 450.85 752.41 C 486.67 752.41 515.71 713.33 515.71 665.13 C 515.71 657.39 514.96 649.89 513.55 642.75"/><path fill="#0b6b45" d="M 390.89 722.09 C 390.89 734.16 381.11 743.94 369.04 743.94 C 356.98 743.94 347.19 734.16 347.19 722.09 C 347.19 710.02 356.98 700.24 369.04 700.24 C 381.11 700.24 390.89 710.02 390.89 722.09"/><path fill="#f6c324" d="M 448.34 702.45 L 448.34 667.30 C 445.56 667.40 442.75 667.46 439.89 667.46 C 394.33 667.46 357.40 655.05 357.40 639.75 C 357.40 626.91 383.43 616.10 418.73 612.96 L 418.73 575.13 C 373.92 577.87 338.68 605.75 338.68 639.75 C 338.68 675.57 377.76 704.61 425.96 704.61 C 433.70 704.61 441.20 703.86 448.34 702.45"/><path fill="#f6c324" d="M 369.00 579.79 C 356.94 579.79 347.16 570.01 347.16 557.94 C 347.16 545.87 356.94 536.09 369.00 536.09 C 381.07 536.09 390.85 545.87 390.85 557.94 C 390.85 570.01 381.07 579.79 369.00 579.79"/><path fill="#0b6b45" d="M 388.64 637.24 L 423.79 637.24 C 423.69 634.46 423.63 631.65 423.63 628.79 C 423.63 583.23 436.04 546.30 451.34 546.30 C 464.19 546.30 474.99 572.33 478.13 607.63 L 515.96 607.63 C 513.23 562.81 485.35 527.58 451.34 527.58 C 415.53 527.58 386.48 566.66 386.48 614.86 C 386.48 622.60 387.23 630.10 388.64 637.24"/><path fill="#0b6b45" d="M 511.30 557.90 C 511.30 545.83 521.08 536.05 533.15 536.05 C 545.22 536.05 555.00 545.83 555.00 557.90 C 555.00 569.97 545.22 579.75 533.15 579.75 C 521.08 579.75 511.30 569.97 511.30 557.90"/><path fill="#f6c324" d="M 563.52 640.23 C 563.52 667.05 541.60 690.06 510.35 699.92 C 513.81 689.26 515.72 677.5 515.72 665.12 C 515.72 663.87 515.70 662.62 515.66 661.38 C 533.5 656.28 544.80 648.70 544.80 640.23 C 544.80 624.93 507.87 612.52 462.31 612.52 C 459.45 612.52 456.63 612.60 453.85 612.69 L 453.85 577.53 C 461 576.12 468.50 575.37 476.24 575.37 C 524.44 575.37 563.52 604.41 563.52 640.23"/><path fill="#f6c324" d="M 533.19 700.20 C 545.26 700.20 555.04 709.98 555.04 722.05 C 555.04 734.12 545.26 743.90 533.19 743.90 C 521.12 743.90 511.34 734.12 511.34 722.05 C 511.34 709.98 521.12 700.20 533.19 700.20"/></svg>'
LOCKUP = '<svg class="lockup" role="img" aria-label="Village Health Access" xmlns="http://www.w3.org/2000/svg" viewBox="336.7 525.6 606.6 228.8"><path fill="#0b6b45" d="M 513.55 642.75 L 478.41 642.75 C 478.50 645.53 478.57 648.34 478.57 651.20 C 478.57 696.76 466.16 733.69 450.85 733.69 C 438.01 733.69 427.21 707.66 424.07 672.36 L 386.23 672.36 C 388.97 717.18 416.85 752.41 450.85 752.41 C 486.67 752.41 515.71 713.33 515.71 665.13 C 515.71 657.39 514.96 649.89 513.55 642.75"/><path fill="#0b6b45" d="M 390.89 722.09 C 390.89 734.16 381.11 743.94 369.04 743.94 C 356.98 743.94 347.19 734.16 347.19 722.09 C 347.19 710.02 356.98 700.24 369.04 700.24 C 381.11 700.24 390.89 710.02 390.89 722.09"/><path fill="#f6c324" d="M 448.34 702.45 L 448.34 667.30 C 445.56 667.40 442.75 667.46 439.89 667.46 C 394.33 667.46 357.40 655.05 357.40 639.75 C 357.40 626.91 383.43 616.10 418.73 612.96 L 418.73 575.13 C 373.92 577.87 338.68 605.75 338.68 639.75 C 338.68 675.57 377.76 704.61 425.96 704.61 C 433.70 704.61 441.20 703.86 448.34 702.45"/><path fill="#f6c324" d="M 369.00 579.79 C 356.94 579.79 347.16 570.01 347.16 557.94 C 347.16 545.87 356.94 536.09 369.00 536.09 C 381.07 536.09 390.85 545.87 390.85 557.94 C 390.85 570.01 381.07 579.79 369.00 579.79"/><path fill="#0b6b45" d="M 388.64 637.24 L 423.79 637.24 C 423.69 634.46 423.63 631.65 423.63 628.79 C 423.63 583.23 436.04 546.30 451.34 546.30 C 464.19 546.30 474.99 572.33 478.13 607.63 L 515.96 607.63 C 513.23 562.81 485.35 527.58 451.34 527.58 C 415.53 527.58 386.48 566.66 386.48 614.86 C 386.48 622.60 387.23 630.10 388.64 637.24"/><path fill="#0b6b45" d="M 511.30 557.90 C 511.30 545.83 521.08 536.05 533.15 536.05 C 545.22 536.05 555.00 545.83 555.00 557.90 C 555.00 569.97 545.22 579.75 533.15 579.75 C 521.08 579.75 511.30 569.97 511.30 557.90"/><path fill="#f6c324" d="M 563.52 640.23 C 563.52 667.05 541.60 690.06 510.35 699.92 C 513.81 689.26 515.72 677.5 515.72 665.12 C 515.72 663.87 515.70 662.62 515.66 661.38 C 533.5 656.28 544.80 648.70 544.80 640.23 C 544.80 624.93 507.87 612.52 462.31 612.52 C 459.45 612.52 456.63 612.60 453.85 612.69 L 453.85 577.53 C 461 576.12 468.50 575.37 476.24 575.37 C 524.44 575.37 563.52 604.41 563.52 640.23"/><path fill="#f6c324" d="M 533.19 700.20 C 545.26 700.20 555.04 709.98 555.04 722.05 C 555.04 734.12 545.26 743.90 533.19 743.90 C 521.12 743.90 511.34 734.12 511.34 722.05 C 511.34 709.98 521.12 700.20 533.19 700.20"/><path fill="#10201a" d="M 650.31 592.19 L 633.28 592.19 L 614.25 533.76 L 628.86 533.76 L 641.80 576.75 L 654.73 533.76 L 669.34 533.76 ZM 650.31 592.19 M 675.19 533.76 L 688.54 533.76 L 688.54 592.19 L 675.19 592.19 ZM 675.19 533.76 M 712.75 533.76 L 712.75 579.34 L 733.62 579.34 L 733.62 592.19 L 699.39 592.19 L 699.39 533.76 ZM 712.75 533.76 M 753.66 533.76 L 753.66 579.34 L 774.52 579.34 L 774.52 592.19 L 740.30 592.19 L 740.30 533.76 ZM 753.66 533.76 M 806.25 549.03 L 799.40 570.49 L 813.09 570.49 ZM 834.63 592.19 L 820.02 592.19 L 817.10 583.01 L 795.39 583.01 L 792.47 592.19 L 777.86 592.19 L 797.73 533.76 L 814.76 533.76 ZM 834.63 592.19 M 866.93 559.64 L 896.23 559.64 L 896.23 564.64 C 896.23 573.33 893.50 580.31 888.05 585.60 C 882.65 590.77 875.78 593.36 867.43 593.36 C 858.36 593.36 850.82 590.44 844.81 584.60 C 838.85 578.75 835.88 571.57 835.88 563.06 C 835.88 554.55 838.83 547.34 844.73 541.44 C 850.62 535.54 857.89 532.59 866.51 532.59 C 871.91 532.59 876.88 533.80 881.41 536.22 C 885.95 538.64 889.50 541.89 892.06 545.95 L 880.71 552.46 C 879.37 550.40 877.44 548.75 874.91 547.49 C 872.37 546.24 869.55 545.61 866.43 545.61 C 861.48 545.61 857.36 547.26 854.08 550.54 C 850.85 553.76 849.23 557.97 849.23 563.14 C 849.23 568.15 850.91 572.30 854.25 575.58 C 857.58 578.75 862.03 580.34 867.60 580.34 C 875.28 580.34 880.26 577.33 882.54 571.32 L 866.93 571.32 ZM 866.93 559.64 M 917.94 568.99 L 917.94 579.34 L 941.31 579.34 L 941.31 592.19 L 904.58 592.19 L 904.58 533.76 L 940.89 533.76 L 940.89 546.62 L 917.94 546.62 L 917.94 556.30 L 938.81 556.30 L 938.81 568.99 ZM 917.94 568.99 M 650.98 633.15 L 650.98 610.78 L 664.33 610.78 L 664.33 669.21 L 650.98 669.21 L 650.98 646.00 L 632.61 646.00 L 632.61 669.21 L 619.26 669.21 L 619.26 610.78 L 632.61 610.78 L 632.61 633.15 ZM 650.98 633.15 M 688.54 646.01 L 688.54 656.35 L 711.92 656.35 L 711.92 669.21 L 675.19 669.21 L 675.19 610.78 L 711.50 610.78 L 711.50 623.63 L 688.54 623.63 L 688.54 633.32 L 709.41 633.32 L 709.41 646.01 ZM 688.54 646.01 M 744.47 626.05 L 737.63 647.51 L 751.32 647.51 ZM 772.85 669.21 L 758.25 669.21 L 755.32 660.03 L 733.62 660.03 L 730.70 669.21 L 716.09 669.21 L 735.96 610.78 L 752.99 610.78 ZM 772.85 669.21 M 792.05 610.78 L 792.05 656.36 L 812.92 656.36 L 812.92 669.21 L 778.70 669.21 L 778.70 610.78 ZM 792.05 610.78 M 809.58 610.78 L 852.99 610.78 L 852.99 623.63 L 837.96 623.63 L 837.96 669.21 L 824.61 669.21 L 824.61 623.63 L 809.58 623.63 ZM 809.58 610.78 M 891.39 633.15 L 891.39 610.78 L 904.75 610.78 L 904.75 669.21 L 891.39 669.21 L 891.39 646.00 L 873.03 646.00 L 873.03 669.21 L 859.67 669.21 L 859.67 610.78 L 873.03 610.78 L 873.03 633.15 ZM 891.39 633.15 M 642.63 703.07 L 635.78 724.53 L 649.48 724.53 ZM 671.01 746.23 L 656.40 746.23 L 653.48 737.05 L 631.78 737.05 L 628.86 746.23 L 614.25 746.23 L 634.12 687.80 L 651.14 687.80 ZM 671.01 746.23 M 702.65 747.40 C 693.91 747.40 686.65 744.51 680.86 738.72 C 675.13 732.93 672.26 725.69 672.26 717.01 C 672.26 708.33 675.13 701.12 680.86 695.39 C 686.59 689.55 693.86 686.63 702.65 686.63 C 707.88 686.63 712.72 687.84 717.17 690.26 C 721.63 692.68 725.13 695.98 727.69 700.15 L 716.17 706.83 C 714.89 704.55 713.07 702.78 710.71 701.53 C 708.34 700.28 705.66 699.65 702.65 699.65 C 697.42 699.65 693.27 701.24 690.21 704.41 C 687.15 707.53 685.62 711.73 685.62 717.01 C 685.62 722.30 687.15 726.50 690.21 729.62 C 693.27 732.79 697.42 734.38 702.65 734.38 C 705.60 734.38 708.28 733.74 710.71 732.46 C 713.12 731.18 714.95 729.42 716.17 727.20 L 727.69 733.88 C 725.19 738.05 721.71 741.35 717.26 743.77 C 712.80 746.19 707.94 747.40 702.65 747.40 M 761.83 747.40 C 753.10 747.40 745.83 744.51 740.05 738.72 C 734.32 732.93 731.45 725.69 731.45 717.01 C 731.45 708.33 734.32 701.12 740.05 695.39 C 745.78 689.55 753.04 686.63 761.83 686.63 C 767.07 686.63 771.91 687.84 776.36 690.26 C 780.81 692.68 784.32 695.98 786.88 700.15 L 775.36 706.83 C 774.08 704.55 772.26 702.78 769.89 701.53 C 767.52 700.28 764.84 699.65 761.83 699.65 C 756.60 699.65 752.46 701.24 749.40 704.41 C 746.33 707.53 744.81 711.73 744.81 717.01 C 744.81 722.30 746.33 726.50 749.40 729.62 C 752.46 732.79 756.60 734.38 761.83 734.38 C 764.78 734.38 767.47 733.74 769.89 732.46 C 772.31 731.18 774.13 729.42 775.36 727.20 L 786.88 733.88 C 784.37 738.05 780.89 741.35 776.44 743.77 C 771.99 746.19 767.12 747.40 761.83 747.40 M 807.33 723.03 L 807.33 733.37 L 830.71 733.37 L 830.71 746.23 L 793.97 746.23 L 793.97 687.80 L 830.29 687.80 L 830.29 700.65 L 807.33 700.65 L 807.33 710.33 L 828.20 710.33 L 828.20 723.03 ZM 807.33 723.03 M 859.50 747.40 C 853.66 747.40 848.73 746.14 844.73 743.60 C 840.72 741.07 837.85 737.52 836.13 732.96 L 847.65 726.28 C 849.99 731.68 854.08 734.38 859.92 734.38 C 865.21 734.38 867.85 732.79 867.85 729.62 C 867.85 727.84 866.99 726.50 865.26 725.61 C 863.48 724.56 860.31 723.41 855.75 722.19 C 851.07 720.91 847.12 719.07 843.89 716.68 C 840.33 713.79 838.55 709.70 838.55 704.41 C 838.55 699.01 840.47 694.70 844.31 691.47 C 848.21 688.25 852.82 686.63 858.17 686.63 C 862.95 686.63 867.18 687.76 870.85 690.01 C 874.53 692.26 877.42 695.53 879.54 699.82 L 868.27 706.41 C 866.15 701.91 862.78 699.65 858.17 699.65 C 856.22 699.65 854.69 700.07 853.58 700.90 C 852.46 701.74 851.91 702.80 851.91 704.08 C 851.91 705.47 852.57 706.72 853.91 707.83 C 855.36 708.94 858.19 710.12 862.42 711.34 L 867.85 713.09 C 869.24 713.54 870.85 714.29 872.69 715.34 C 874.70 716.35 876.20 717.43 877.20 718.60 C 879.87 721.5 881.21 725.11 881.21 729.45 C 881.21 734.96 879.20 739.36 875.20 742.64 C 871.19 745.82 865.96 747.40 859.50 747.40 M 907.50 747.40 C 901.66 747.40 896.73 746.14 892.73 743.60 C 888.72 741.07 885.85 737.52 884.13 732.96 L 895.65 726.28 C 897.99 731.68 902.08 734.38 907.92 734.38 C 913.21 734.38 915.85 732.79 915.85 729.62 C 915.85 727.84 914.99 726.50 913.26 725.61 C 911.48 724.56 908.31 723.41 903.75 722.19 C 899.07 720.91 895.12 719.07 891.89 716.68 C 888.33 713.79 886.55 709.70 886.55 704.41 C 886.55 699.01 888.47 694.70 892.31 691.47 C 896.20 688.25 900.82 686.63 906.17 686.63 C 910.95 686.63 915.18 687.76 918.85 690.01 C 922.53 692.26 925.42 695.53 927.54 699.82 L 916.27 706.41 C 914.15 701.91 910.78 699.65 906.17 699.65 C 904.22 699.65 902.69 700.07 901.58 700.90 C 900.46 701.74 899.91 702.80 899.91 704.08 C 899.91 705.47 900.57 706.72 901.91 707.83 C 903.35 708.94 906.19 710.12 910.42 711.34 L 915.85 713.09 C 917.24 713.54 918.85 714.29 920.69 715.34 C 922.69 716.35 924.20 717.43 925.20 718.60 C 927.87 721.5 929.21 725.11 929.21 729.45 C 929.21 734.96 927.20 739.36 923.19 742.64 C 919.19 745.82 913.96 747.40 907.50 747.40"/></svg>'

NAV = [("about.html", "About"), ("programs.html", "Programs"), ("impact.html", "Impact"),
       ("partners.html", "Partners"), ("news.html", "News"), ("contact.html", "Contact")]


def icon(d):
    return (f'<span class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{d}</svg></span>')


I_PHONE = icon('<rect x="6" y="2" width="12" height="20" rx="2.5"/><path d="M11 18h2"/><path d="M12 7v6M9 10h6"/>')
I_PILL = icon('<path d="M10.5 3.5a5 5 0 0 1 7 7l-7 7a5 5 0 0 1-7-7z"/><path d="m7 10 7 7"/>')
I_GOV = icon('<path d="M3 21h18M5 21V10M19 21V10M9.5 21V10M14.5 21V10M2 10l10-7 10 7z"/>')
I_DROP = icon('<path d="M12 2.5S5 10 5 14.5a7 7 0 0 0 14 0C19 10 12 2.5 12 2.5z"/><path d="M9 15h6M12 12v6"/>')
I_HEART = icon('<path d="M20.5 8.5c0 5-8.5 11-8.5 11s-8.5-6-8.5-11A4.5 4.5 0 0 1 12 6a4.5 4.5 0 0 1 8.5 2.5z"/>')
I_HAND = icon('<path d="M3 13h3l4 3h5a2 2 0 0 0 0-4h-3"/><path d="M6 13v7H3M14 12l5-2a2 2 0 0 1 2 3l-7 5H10"/>')
I_USERS = icon('<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><path d="M16 4.5a3.5 3.5 0 0 1 0 7M18.5 20a6.5 6.5 0 0 0-3-5.5"/>')
I_SPARK = icon('<path d="M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2.5 2.5M15.5 15.5 18 18M6 18l2.5-2.5M15.5 8.5 18 6"/>')
I_SCALE = icon('<path d="M12 3v18M5 21h14M4 7h16"/><path d="m4 7-2.5 6a3 3 0 0 0 5 0zM20 7l-2.5 6a3 3 0 0 0 5 0z"/>')
I_MAIL = icon('<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3.5 6 8.5 7 8.5-7"/>')
I_MIC = icon('<rect x="9" y="2" width="6" height="12" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v4"/>')

LANGS = ["French", "English", "Ewe", "Hausa", "Yoruba", "Twi", "Mooré", "Bambara", "and local dialects"]
LANG_CHIPS = "".join(f"<li>{l}</li>" for l in LANGS)


def copy_row(addr):
    return f'<div class="copy-row"><code>{addr}</code><button class="copy-btn" type="button" data-copy="{addr}">Copy</button></div>'


CTA = '''<section class="band cta"><div class="wrap"><div class="cta-inner">
  <div style="display:grid;gap:.8rem"><p class="eyebrow">Support us</p><h2>Help healthcare reach the villages clinics can't.</h2></div>
  <div class="actions" style="margin:0"><a class="btn btn-gold" href="donate.html">Donate</a><a class="btn btn-ghost" href="donate.html#grants">Grant opportunities</a></div>
</div></div></section>'''

GOALS = '''<div class="goals">
  <div class="goal"><b>10,000+</b><span>families reached</span></div>
  <div class="goal"><b>7</b><span>West African countries</span></div>
  <div class="goal"><b>14</b><span>languages of care</span></div>
  <div class="goal"><b>500+</b><span>partner clinics and pharmacies</span></div>
</div>'''

# ---------------------------------------------------------------- HOME
HOME = f'''
<section class="band hero"><div class="wrap hero-grid">
  <div>
    <p class="pill"><span class="pill-dot"></span>In partnership with Verakou</p>
    <h1>Healthcare for <span class="hl">every village.</span></h1>
    <p class="lead">Free telemedicine and essential medicines for underserved communities across West Africa, delivered over the phones people already use, in the languages they speak.</p>
    <div class="actions"><a class="btn btn-gold" href="donate.html">Support our mission</a><a class="btn btn-ghost" href="programs.html">See our programs</a></div>
    <ul class="trust">
      <li><b>Free</b> for patients</li>
      <li><b>WhatsApp</b> first</li>
      <li><b>Licensed</b> clinicians</li>
    </ul>
  </div>
  <div class="hero-visual">
    <div class="phone" role="img" aria-label="Illustration of a WhatsApp consultation">
      <div class="phone-notch"></div>
      <div class="chat">
        <div class="chat-head"><span class="dot logo-dot">{LOGO}</span><div><b>Village Health Access</b><span>online</span></div></div>
        <div class="msg out">Good morning. My daughter has had a fever since yesterday.<i>Patient · translated from Ewe</i></div>
        <div class="msg in">Thank you. How old is she, and has she been tested for malaria?<i>Community health worker</i></div>
        <div class="msg in">A licensed clinician will review her case today.<i>Care coordination</i></div>
      </div>
    </div>
    <div class="float float-a"><span class="float-ic ok">✓</span><div><b>Clinician assigned</b><small>Reviewing case</small></div></div>
    <div class="float float-b"><span class="float-ic rx">Rx</span><div><b>Medicine ready</b><small>Partner pharmacy</small></div></div>
    <p class="visual-note">Illustration of how a consultation works</p>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><p class="eyebrow">How it works</p><h2>From a message to medicine, without the long walk.</h2></div>
  <ol class="steps">
    <li><h3>Reach out by WhatsApp</h3><p>Patients connect through WhatsApp and digital health platforms, in their own language. No clinic visit or travel is needed to start.</p></li>
    <li><h3>Get triaged and seen</h3><p>A multilingual triage protocol routes each case to a licensed clinician for diagnosis, treatment and follow-up.</p></li>
    <li><h3>Receive medicine</h3><p>Prescriptions are filled through our network of licensed partner pharmacies, at no cost to the patient.</p></li>
  </ol>
</div></section>

<section class="section section-alt"><div class="wrap">
  <div class="section-head"><p class="eyebrow">What we do</p><h2>Four programs, one goal: healthcare people can reach.</h2></div>
  <div class="grid g4">
    <article class="card">{I_PHONE}<h3>Telemedicine Access</h3><p>Free and subsidized virtual consultations for orphans, refugees, rural farmers and the urban poor.</p><a class="more" href="programs.html#telemedicine">Learn more →</a></article>
    <article class="card">{I_PILL}<h3>Essential Medicines</h3><p>Prescriptions filled at no cost, with a focus on HIV, TB, malaria and maternal health.</p><a class="more" href="programs.html#medicines">Learn more →</a></article>
    <article class="card">{I_GOV}<h3>Government Integration</h3><p>Working with health ministries to formalize community health worker networks and share surveillance data.</p><a class="more" href="programs.html#government">Learn more →</a></article>
    <article class="card">{I_DROP}<h3>Cholera &amp; Vaccines</h3><p>Cholera response in Togo and last-mile vaccine delivery to communities with no health facility.</p><a class="more" href="programs.html#cholera">Learn more →</a></article>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="grid g2" style="gap:3rem;align-items:start">
    <div class="prose">
      <p class="eyebrow">Our mission</p>
      <h2>Care that doesn't depend on income, location or language.</h2>
      <p>We provide free, high-quality telemedicine and essential medicines to the most underserved communities in West Africa. We launch in Togo at the end of 2027 and are building toward rural, refugee and urban-poor communities across the region.</p>
      <p><a href="about.html">Read our story →</a></p>
    </div>
    <div style="display:grid;gap:1rem">
      <p class="eyebrow">Our 2030 goals</p>
      {GOALS.replace('class="goals"', 'class="goals two"')}
      <p class="small muted">These are goals, not results. We publish progress on our <a href="impact.html">impact page</a>.</p>
    </div>
  </div>
</div></section>

<section class="section section-alt"><div class="wrap">
  <div class="section-head" style="grid-template-columns:1fr auto;max-width:none;align-items:end"><div style="display:grid;gap:.7rem"><p class="eyebrow">News</p><h2>Latest updates</h2></div><a class="more" style="font-weight:700" href="news.html">All updates →</a></div>
  <div class="grid g3">
    <article class="card post"><time datetime="2026-08">August 2026</time><h3>WHO calls for urgent scale-up of cholera vaccines across West Africa</h3><p>An emergency call as cholera cases rise in Togo, Benin and Nigeria.</p></article>
    <article class="card post"><time datetime="2026-07">July 2026</time><h3>Togo launches national community health worker program</h3><p>A Ministry of Health framework for community health workers, open to NGOs and digital platforms.</p></article>
    <article class="card post"><time datetime="2026-06">June 2026</time><h3>Telemedicine adoption rising across francophone Africa</h3><p>An ECOWAS report points to sharp growth in WhatsApp-based consultations.</p></article>
  </div>
</div></section>
{CTA}
'''

# ---------------------------------------------------------------- ABOUT
ABOUT = f'''
<section class="band page-hero"><div class="wrap">
  <p class="eyebrow">Who we are</p>
  <h1>About Village Health Access</h1>
  <p class="lead">A humanitarian initiative, in partnership with Verakou, bringing quality healthcare to the most vulnerable communities in West Africa.</p>
</div></section>

<section class="section"><div class="wrap grid g2" style="gap:3rem">
  <div class="prose">
    <p class="eyebrow">Our story</p>
    <h2>Born from what we saw firsthand.</h2>
    <p>Donald Daglo founded Village Health Access after seeing patients in Togo turned away from clinics because they could not afford care or could not reach it.</p>
    <p>Families were choosing between food and medicine. People walked for hours to reach clinics that were closed or out of stock. Across Togo, Ghana, Benin and beyond, the gap in access to care is wide.</p>
    <p>Village Health Access closes that gap with telemedicine, a network of partner pharmacies and community health workers, reaching people where they already are.</p>
    <p class="small muted">West Africa · launching end of 2027</p>
  </div>
  <div style="display:grid;gap:1.25rem;align-content:start">
    <div class="panel"><p class="eyebrow">Mission</p><p style="font-size:1.2rem">To provide free telemedicine and access to essential medicines for the most vulnerable communities in West Africa.</p></div>
    <div class="panel"><p class="eyebrow">Vision</p><p style="font-size:1.2rem">A world where geography and income never determine health outcomes.</p></div>
  </div>
</div></section>

<section class="section section-alt"><div class="wrap">
  <div class="section-head"><p class="eyebrow">Our values</p><h2>What guides our work</h2></div>
  <div class="grid g4">
    <div class="card">{I_SCALE}<h3>Equity</h3><p>Everyone deserves quality care, whatever their income, location or language.</p></div>
    <div class="card">{I_HEART}<h3>Compassion</h3><p>We treat every patient with dignity and respect.</p></div>
    <div class="card">{I_SPARK}<h3>Innovation</h3><p>WhatsApp triage and multilingual support built for low-connectivity areas.</p></div>
    <div class="card">{I_HAND}<h3>Accountability</h3><p>Monthly impact data, financial transparency and measurable outcomes.</p></div>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><p class="eyebrow">Leadership</p><h2>Board of Directors</h2><p class="muted">We are recruiting board members. If you have the experience below, we'd like to hear from you.</p></div>
  <div class="grid g3">
    <div class="card"><div class="person"><span class="avatar">DD</span><div style="display:grid;gap:.3rem"><h3>Donald Daglo</h3><p class="small"><b>Founder &amp; Executive Director</b></p><p class="small">Also leads Klinova, the health technology platform that supports VHA's programs.</p></div></div></div>
    <div class="card"><div class="person"><span class="avatar open">+</span><div style="display:grid;gap:.3rem"><h3>Medical Advisory Board</h3><p class="small"><b>Recruiting</b></p><p class="small">Licensed clinicians and public health leaders from West Africa.</p></div></div></div>
    <div class="card"><div class="person"><span class="avatar open">+</span><div style="display:grid;gap:.3rem"><h3>Finance &amp; Governance</h3><p class="small"><b>Recruiting</b></p><p class="small">Nonprofit finance and 501(c)(3) governance experience.</p></div></div></div>
  </div>
  <p style="margin-top:1.5rem"><a class="btn btn-line" href="contact.html">Express interest in joining</a></p>
</div></section>

<section class="section section-alt"><div class="wrap grid g2" style="gap:3rem;align-items:center">
  <div class="prose">
    <p class="eyebrow">How we're organized</p>
    <h2>In partnership with Verakou. Powered by Klinova.</h2>
    <p>Village Health Access works in partnership with Verakou. Our telemedicine service is powered by Klinova, built on the Kinara platform.</p>
  </div>
  <div style="display:grid;gap:1rem">
    <div class="panel"><p class="eyebrow">Technology</p><h2 class="h3">Powered by Klinova, built on the Kinara platform</h2><p class="muted">Klinova provides the technology behind our programs: a WhatsApp-based, multilingual triage and care coordination system designed for low-connectivity areas.</p><p><a href="https://klinova.co">Visit klinova.co</a></p></div>
  </div>
</div></section>
{CTA}
'''

# ---------------------------------------------------------------- PROGRAMS
PROGRAMS = f'''
<section class="band page-hero"><div class="wrap">
  <p class="eyebrow">What we do</p>
  <h1>Programs built for the communities that need them most.</h1>
  <p class="lead">Four programs that address distance, cost, disconnection and preventable disease.</p>
</div></section>

<section class="section"><div class="wrap">

  <article class="program" id="telemedicine">
    <div class="prose">
      {I_PHONE}
      <h2>Telemedicine Access</h2>
      <p>Free and subsidized virtual consultations for orphans, refugees, rural farmers and the urban poor.</p>
      <p>Patients connect by app or WhatsApp. A community health worker completes a structured, multilingual triage and escalates to a licensed clinician for diagnosis, treatment and follow-up.</p>
    </div>
    <div class="side">
      <div class="panel"><p class="eyebrow">Languages of care</p><p class="muted small">Our translation network is planned to cover 14 languages, including:</p><ul class="chips">{LANG_CHIPS}</ul></div>
      <div class="panel"><p class="eyebrow">Where</p><p>Launching in Togo at the end of 2027, then expanding to Ghana, Benin and beyond, with a goal of 7 countries by 2030.</p></div>
    </div>
  </article>

  <article class="program" id="medicines">
    <div class="prose">
      {I_PILL}
      <h2>Essential Medicines</h2>
      <p>Prescriptions from telemedicine consultations are filled at no cost to the patient.</p>
      <p>We work through licensed pharmacies and government supply chains using WHO-prequalified medicines, with cold-chain handling for temperature-sensitive drugs through regional distributors.</p>
    </div>
    <div class="side"><div class="panel"><p class="eyebrow">Focus areas</p>
      <ul class="list"><li>HIV antiretroviral treatment</li><li>Tuberculosis care</li><li>Malaria prevention and treatment</li><li>Maternal and newborn health</li><li>Childhood immunization support</li></ul>
    </div></div>
  </article>

  <article class="program" id="government">
    <div class="prose">
      {I_GOV}
      <h2>Government Integration</h2>
      <p>We aim to formalize community health worker networks with West African health ministries, share surveillance data and integrate telemedicine protocols into public health systems.</p>
      <p>We are in active conversations with health authorities in Togo, Ghana, Benin and Nigeria. No agreements have been signed yet.</p>
      <p><a class="btn btn-line" href="impact.html">View our impact data</a></p>
    </div>
    <div class="side"><div class="panel"><p class="eyebrow">What we will share with ministries</p>
      <ul class="list"><li>Anonymized disease surveillance data</li><li>Community health worker coverage maps</li><li>Medicine supply status reports</li><li>Outbreak early-warning indicators</li><li>Consultation volume by region</li></ul>
    </div></div>
  </article>

  <article class="program" id="cholera">
    <div class="prose">
      {I_DROP}
      <h2>Combating Cholera &amp; Delivering Vaccines</h2>
      <p>Our cholera response in Togo will combine oral rehydration, sanitation education and rapid deployment of community health workers.</p>
      <p>We will deliver vaccines to the last mile, including nomadic groups, refugee camps and villages with no health facility. Outbreak data will be logged on our platform for reporting to health authorities.</p>
    </div>
    <div class="side"><div class="panel"><p class="eyebrow">Vaccination programs</p>
      <ul class="list"><li>Cholera</li><li>Meningitis</li><li>Yellow fever</li><li>Routine childhood immunizations</li></ul>
    </div></div>
  </article>

</div></section>

<section class="section section-alt"><div class="wrap">
  <div class="section-head"><p class="eyebrow">Get involved</p><h2>There's a place for you in this work.</h2></div>
  <div class="grid g3">
    <div class="card">{I_HAND}<h3>Partner with us</h3><p>Clinics, pharmacies, NGOs and health agencies can join our referral and supply network.</p><a class="more" href="partners.html">Apply to partner →</a></div>
    <div class="card">{I_HEART}<h3>Donate</h3><p>Fund consultations, medicines and community health workers.</p><a class="more" href="donate.html">Support the mission →</a></div>
    <div class="card">{I_USERS}<h3>Volunteer</h3><p>We welcome licensed clinicians, translators, data analysts and public health professionals.</p><a class="more" href="contact.html">Get in touch →</a></div>
  </div>
</div></section>
'''

# ---------------------------------------------------------------- IMPACT
ROADMAP = [
    ("live", "Togo", "End of 2027", "Our first country, launching at the end of 2027."),
    ("", "Ghana", "Planned", "Next expansion country."),
    ("", "Benin", "Planned", "Next expansion country."),
    ("", "Nigeria", "Planned", "In conversation with health authorities."),
    ("", "Burkina Faso", "2028", "Expansion roadmap."),
    ("", "Côte d'Ivoire", "2028", "Expansion roadmap."),
    ("", "Senegal", "2029", "Expansion roadmap."),
]
ROADMAP_HTML = "".join(
    f'<li class="{c}"><div class="row"><h3>{n}</h3><span class="tag{" live" if c else ""}">{s}</span></div><p class="muted small">{d}</p></li>'
    for c, n, s, d in ROADMAP)

DISEASE = [("Fever / malaria", 34), ("Respiratory", 22), ("Digestive", 18), ("Maternal health", 12), ("Other", 14)]
BARS = "".join(
    f'<div class="bar"><span>{n}</span><div class="bar-track"><div class="bar-fill" style="width:{v / 34 * 100:.0f}%"></div></div><b>{v}%</b></div>'
    for n, v in DISEASE)

IMPACT = f'''
<section class="band page-hero"><div class="wrap">
  <p class="eyebrow">Measuring what matters</p>
  <h1>Our impact, reported honestly.</h1>
  <p class="lead">We are a young initiative. We launch in Togo at the end of 2027. Here is where we're going, what we'll measure, and how we'll report progress each month.</p>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><p class="eyebrow">2030 goals</p><h2>What we're working toward</h2></div>
  <div class="goals">
    <div class="goal"><b>10,000+</b><span>consultations</span></div>
    <div class="goal"><b>12,000+</b><span>medicine packages</span></div>
    <div class="goal"><b>500+</b><span>partner clinics</span></div>
    <div class="goal"><b>14</b><span>languages</span></div>
  </div>
  <div class="panel" style="margin-top:1.25rem"><p class="eyebrow">Results</p><p>We launch in Togo at the end of 2027. From then on we will publish consultations completed, medicine packages delivered and families served here every month.</p></div>
</div></section>

<section class="section section-alt"><div class="wrap grid g2" style="gap:3rem">
  <div>
    <div class="section-head"><p class="eyebrow">Where we work</p><h2>Country roadmap</h2></div>
    <ol class="roadmap">{ROADMAP_HTML}</ol>
  </div>
  <div>
    <div class="section-head"><p class="eyebrow">Consultations</p><h2>What we will report</h2></div>
    <div class="panel"><p>After launch, we will publish the share of consultations by category each month: fever and malaria, respiratory illness, digestive illness, maternal health and other conditions.</p>
    <p class="small muted">All data will be anonymized before it is published.</p></div>
  </div>
</div></section>

<section class="section"><div class="wrap grid g2" style="gap:2rem">
  <div class="panel"><p class="eyebrow">Data transparency</p><h3>Updated monthly, always anonymized</h3><p class="muted">Impact data is updated monthly. Patient data is anonymized and never shared publicly. <a href="privacy.html">Read our privacy commitments</a>.</p></div>
  <div class="panel" id="annual-report"><p class="eyebrow">Annual report</p><h3>First annual report</h3><p class="muted">Our first annual report will be published here after our first year of operations, which begins with our launch at the end of 2027.</p></div>
</div></section>
{CTA}
'''

# ---------------------------------------------------------------- PARTNERS
PARTNERS = f'''
<section class="band page-hero"><div class="wrap">
  <p class="eyebrow">Building our network</p>
  <h1>Partner with Village Health Access</h1>
  <p class="lead">We are building a network of clinics, pharmacies, NGOs and health agencies so that a WhatsApp message can turn into real care.</p>
</div></section>

<section class="section"><div class="wrap">
  <div class="panel" style="margin-bottom:2.5rem;max-width:44rem"><p class="eyebrow">Partnership &amp; technology</p><h2 class="h3">In partnership with Verakou. Powered by Klinova.</h2><p class="muted">Village Health Access works in partnership with Verakou. Klinova, built on the Kinara platform, provides the WhatsApp-based triage and care coordination technology our programs run on.</p></div>
  <div class="section-head"><p class="eyebrow">Who we work with</p><h2>Partnerships we're building</h2></div>
  <div class="grid g4">
    <div class="card">{I_HEART}<h3>Clinics &amp; health facilities</h3><p>Receive referrals and support follow-up care.</p></div>
    <div class="card">{I_PILL}<h3>Pharmacies &amp; distributors</h3><p>Fill prescriptions and join our medicine supply coordination.</p></div>
    <div class="card">{I_USERS}<h3>NGOs &amp; civil society</h3><p>Extend reach into refugee, rural and urban-poor communities.</p></div>
    <div class="card">{I_GOV}<h3>Government health agencies</h3><p>We're in conversation with health authorities in Togo, Ghana, Benin and Nigeria.</p></div>
  </div>
</div></section>

<section class="section section-alt"><div class="wrap grid g2" style="gap:3rem">
  <div class="prose">
    <p class="eyebrow">What partners get</p>
    <h2>Become a partner</h2>
    <ul class="list"><li>Access to our patient referral network</li><li>Medicine supply coordination</li><li>Training</li><li>Community health worker support</li></ul>
    <p>Prefer email? Write to us directly.</p>
    {copy_row("partners@villagehealthaccess.org")}
  </div>
  <div class="panel">
    <form data-mailto="partners@villagehealthaccess.org" data-subject="Partnership request">
      <div class="field"><label for="p-org">Organization name <span class="req">*</span></label><input id="p-org" name="organization" required></div>
      <div class="field"><label for="p-country">Country <span class="req">*</span></label><input id="p-country" name="country" required></div>
      <div class="field"><label for="p-email">Contact email <span class="req">*</span></label><input id="p-email" name="email" type="email" required></div>
      <div class="field"><label for="p-type">Type of partnership</label>
        <select id="p-type" name="partnership_type"><option>Clinic / healthcare facility</option><option>Pharmacy / medicine distributor</option><option>NGO / civil society</option><option>Government health agency</option><option>Community health worker program</option><option>Other</option></select></div>
      <div class="field"><label for="p-msg">Tell us about your organization</label><textarea id="p-msg" name="message"></textarea></div>
      <button class="btn btn-gold" type="submit">Submit partnership request</button>
    </form>
    <p class="form-status small" aria-live="polite"></p>
  </div>
</div></section>
'''

# ---------------------------------------------------------------- DONATE
DONATE = f'''
<section class="band page-hero"><div class="wrap">
  <p class="eyebrow">Support our work</p>
  <h1>Fund healthcare for the unreachable.</h1>
  <p class="lead">Every gift goes to direct program delivery: consultations, medicines and community health workers.</p>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><p class="eyebrow">What your gift does</p><h2>The impact of your donation</h2></div>
  <div class="amounts">
    <div class="card amount"><b>$25</b><h3>One consultation</h3><p>A telemedicine consultation with a licensed clinician.</p></div>
    <div class="card amount"><b>$100</b><h3>A month of medicine for a child</h3><p>Malaria or TB treatment, or nutritional supplements.</p></div>
    <div class="card amount"><b>$500</b><h3>A community health program</h3><p>One community health worker serving a remote village for a month.</p></div>
  </div>
</div></section>

<section class="section section-alt"><div class="wrap grid g2" style="gap:3rem">
  <div class="prose">
    <p class="eyebrow">How to give today</p>
    <h2>Make a donation</h2>
    <p>Our 501(c)(3) application is pending, and secure online giving will open once it is approved. Until then, email us and we will arrange your donation directly and send you a receipt.</p>
    {copy_row("contact@villagehealthaccess.org")}
    <p class="small muted">Tax deductibility depends on our 501(c)(3) approval. Please consult your tax advisor.</p>
  </div>
  <div class="panel amount-picker">
    <p class="eyebrow">Choose an amount</p>
    <div class="actions" style="margin:0">
      <button class="btn btn-line" type="button" data-amount="25" aria-pressed="false">$25</button>
      <button class="btn btn-line" type="button" data-amount="50" aria-pressed="false">$50</button>
      <button class="btn btn-line" type="button" data-amount="100" aria-pressed="true">$100</button>
      <button class="btn btn-line" type="button" data-amount="250" aria-pressed="false">$250</button>
    </div>
    <form data-mailto="contact@villagehealthaccess.org" data-subject="Donation pledge">
      <div class="field"><label for="d-name">Your name</label><input id="d-name" name="name" required></div>
      <div class="field"><label for="d-amount">Amount (USD)</label><input id="d-amount" name="amount" inputmode="decimal" placeholder="Or enter your own amount"></div>
      <button class="btn btn-gold" type="submit">Pledge <span data-amount-out>$100</span> by email</button>
    </form>
    <p class="form-status small" aria-live="polite"></p>
  </div>
</div></section>

<section class="section" id="grants"><div class="wrap grid g2" style="gap:3rem">
  <div class="prose">
    <p class="eyebrow">Institutional funding</p>
    <h2>Grant opportunities</h2>
    <p>We welcome proposals from foundations, bilateral and multilateral donors and impact investors, for both restricted and unrestricted funding.</p>
    <p>Email us with the subject "Grant Information Request".</p>
    {copy_row("contact@villagehealthaccess.org")}
  </div>
  <div class="panel"><p class="eyebrow">Restricted funding areas</p>
    <ul class="list"><li>Telemedicine infrastructure expansion</li><li>Community health worker training and deployment</li><li>Essential medicine supply chain</li><li>Maternal and child health</li><li>Disease surveillance and public health data</li><li>Multi-country replication</li></ul>
  </div>
</div></section>

<section class="section section-alt"><div class="wrap grid g2" style="gap:3rem">
  <div>
    <div class="section-head"><p class="eyebrow">Thank you</p><h2>Current supporters</h2></div>
    <div class="grid" style="gap:.8rem">
      <div class="panel"><h3>Verakou</h3><p class="muted small">Partner</p></div>
      <div class="panel"><h3>Klinova</h3><p class="muted small">In-kind technology partner</p></div>
      <div class="panel"><h3>Founding Friends Fund</h3><p class="muted small">Individual donors</p></div>
      <div class="panel"><h3>West Health Foundation</h3><p class="muted small">Early-stage funder</p></div>
    </div>
  </div>
  <div>
    <div class="section-head"><p class="eyebrow">Financial transparency</p><h2>Where the money goes</h2></div>
    <div class="goals" style="grid-template-columns:repeat(2,minmax(0,1fr))">
      <div class="goal"><b>85%+</b><span>to programs (target)</span></div>
      <div class="goal"><b>&lt;15%</b><span>overhead (target)</span></div>
    </div>
    <p class="muted" style="margin-top:1rem">We publish financial reporting, and full financial statements are available on request.</p>
  </div>
</div></section>
'''

# ---------------------------------------------------------------- NEWS
NEWS = f'''
<section class="band page-hero"><div class="wrap">
  <p class="eyebrow">Updates</p>
  <h1>News &amp; updates</h1>
  <p class="lead">Regional health news, disease alerts, policy and technology that shape our work, plus updates from the field.</p>
</div></section>

<section class="section"><div class="wrap" style="max-width:860px">
  <div style="display:grid;gap:1.25rem">
    <article class="card post"><time datetime="2026-08">August 2026 · Disease alert</time><h2 style="font-size:1.6rem">WHO calls for urgent scale-up of cholera vaccines across West Africa</h2><p>The World Health Organization issued an emergency call to scale up cholera vaccination as cases rise in Togo, Benin and Nigeria. Cholera response is one of our four programs.</p><a class="more" href="programs.html#cholera">Our cholera &amp; vaccine program →</a></article>
    <article class="card post"><time datetime="2026-07">July 2026 · Policy</time><h2 style="font-size:1.6rem">Togo launches national community health worker program</h2><p>Togo's Ministry of Health introduced a national framework for community health workers that is open to NGOs and digital health platforms.</p><a class="more" href="programs.html#government">Our government integration work →</a></article>
    <article class="card post"><time datetime="2026-06">June 2026 · Technology</time><h2 style="font-size:1.6rem">Telemedicine adoption rising across francophone Africa</h2><p>An ECOWAS report describes a 340% rise in WhatsApp-based consultations across francophone Africa.</p><a class="more" href="programs.html#telemedicine">Our telemedicine program →</a></article>
  </div>
  <div class="panel" style="margin-top:2.5rem"><p class="eyebrow">Stay informed</p><h3>Get monthly impact updates</h3><p class="muted">Program milestones, field stories and policy news, once a month. Sign up in the footer below.</p></div>
</div></section>
'''

# ---------------------------------------------------------------- CONTACT
CONTACT = f'''
<section class="band page-hero"><div class="wrap">
  <p class="eyebrow">Reach us</p>
  <h1>Get in touch.</h1>
  <p class="lead">Whether you want to partner, donate, volunteer or learn more, we reply within 2 business days.</p>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><p class="eyebrow">Find the right inbox</p><h2>Email us directly</h2></div>
  <div class="grid g3">
    <div class="card">{I_MAIL}<h3>General inquiries</h3><p>Questions, donations and volunteering.</p>{copy_row("contact@villagehealthaccess.org")}</div>
    <div class="card">{I_HAND}<h3>Partnerships</h3><p>Clinics, pharmacies, NGOs and government.</p>{copy_row("partners@villagehealthaccess.org")}</div>
    <div class="card">{I_MIC}<h3>Media</h3><p>Press and interview requests.</p>{copy_row("media@villagehealthaccess.org")}</div>
  </div>
</div></section>

<section class="section section-alt"><div class="wrap grid g2" style="gap:3rem">
  <div class="panel">
    <h2 style="font-size:1.6rem">Send us a message</h2>
    <form data-mailto="contact@villagehealthaccess.org" data-subject="Website message">
      <div class="field"><label for="c-name">Full name <span class="req">*</span></label><input id="c-name" name="name" required></div>
      <div class="field"><label for="c-email">Email <span class="req">*</span></label><input id="c-email" name="email" type="email" required></div>
      <div class="field"><label for="c-subject">Subject</label><select id="c-subject" name="subject"><option>General</option><option>Partnership</option><option>Donation</option><option>Volunteering</option><option>Media</option><option>Other</option></select></div>
      <div class="field"><label for="c-msg">Message <span class="req">*</span></label><textarea id="c-msg" name="message" required></textarea></div>
      <button class="btn btn-gold" type="submit">Send message</button>
    </form>
    <p class="form-status small" aria-live="polite"></p>
  </div>
  <div style="display:grid;gap:1.25rem;align-content:start">
    <div class="prose"><p class="eyebrow">Where we are</p><h2 style="font-size:1.6rem">Distributed across West Africa</h2><p>We don't have a central office. Our team works where our patients are. We launch in Togo at the end of 2027 and are building toward Ghana, Benin, Nigeria, Burkina Faso, Côte d'Ivoire and Senegal.</p></div>
    <div class="panel"><p class="eyebrow">Follow our work</p>
      <ul class="list" style="list-style:none;padding:0">
        <li><a href="https://x.com/villagehealthacc">X (Twitter) · @villagehealthacc</a></li>
        <li><a href="https://linkedin.com/company/village-health-access">LinkedIn · Village Health Access</a></li>
        <li>WhatsApp · <span class="ph">public WhatsApp number</span></li>
      </ul>
    </div>
  </div>
</div></section>
'''

# ---------------------------------------------------------------- PRIVACY
PRIVACY = '''
<section class="band page-hero"><div class="wrap">
  <p class="eyebrow">Privacy</p>
  <h1>Our privacy commitments</h1>
</div></section>
<section class="section"><div class="wrap prose">
  <p>Patient data is anonymized before it is used in any reporting, and it is never shared publicly.</p>
  <p>Data we share with health authorities, such as disease surveillance figures, is anonymized and aggregated.</p>
  <p><span class="ph">full privacy policy, reviewed by counsel</span></p>
  <p>Questions about your data? Email contact@villagehealthaccess.org.</p>
</div></section>
'''

PAGES = {
    "home": ("index.html", "Home", HOME),
    "about": ("about.html", "About", ABOUT),
    "programs": ("programs.html", "Programs", PROGRAMS),
    "impact": ("impact.html", "Impact", IMPACT),
    "partners": ("partners.html", "Partners", PARTNERS),
    "donate": ("donate.html", "Donate", DONATE),
    "news": ("news.html", "News", NEWS),
    "contact": ("contact.html", "Contact", CONTACT),
    "privacy": ("privacy.html", "Privacy", PRIVACY),
}
