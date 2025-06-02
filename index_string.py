index_string = """
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <style>
            body {
                font-family: 'Inter', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background-color: #f5f5f5;
                margin: 0;
                padding: 0;
            }
            
            .header-gradient {
                background: linear-gradient(135deg, #6b46c1 0%, #3b82f6 100%);
                color: white;
                padding: 20px 0;
            }
            
            .nav-step {
                background: rgba(255, 255, 255, 0.2);
                padding: 15px 30px;
                margin: 0 2px;
                border-radius: 8px;
                font-weight: 500;
                transition: all 0.3s ease;
                cursor: pointer;
                border: none;
                color: white;
            }
            
            .nav-step:hover {
                background: rgba(255, 255, 255, 0.3);
            }
            
            .nav-step.active {
                background: rgba(255, 255, 255, 0.4);
            }
            
            .logo-circle {
                width: 50px;
                height: 50px;
                background: white;
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 24px;
                font-weight: bold;
                color: #6b46c1;
                margin-right: 15px;
            }
            
            .sprout-text {
                font-size: 24px;
                font-weight: 300;
                letter-spacing: 2px;
                color: white;
            }
            
            .select-target-btn {
                background: #1e293b;
                color: white;
                border: none;
                padding: 15px 30px;
                font-size: 14px;
                font-weight: 600;
                cursor: pointer;
                letter-spacing: 1px;
                transition: all 0.3s ease;
                margin-left: 20px;
            }
            
            .select-target-btn:hover {
                background: #334155;
                color: white;
            }
            
            .content-card {
                background: white;
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
                margin-bottom: 30px;
                transition: all 0.2s ease;
            }
            
            .content-card:hover {
                transform: translateY(-2px);
                box-shadow: 0 8px 30px rgba(0, 0, 0, 0.15);
            }
            
            .sidebar-card {
                background: white;
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
                height: fit-content;
            }
            
            .action-card {
                background: white;
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
                text-align: center;
                height: fit-content;
            }
            
            .start-btn {
                background: linear-gradient(135deg, #6b46c1 0%, #3b82f6 100%);
                color: white;
                border: none;
                padding: 20px 40px;
                font-size: 18px;
                font-weight: 600;
                border-radius: 8px;
                cursor: pointer;
                margin-bottom: 20px;
                width: 100%;
                transition: all 0.3s ease;
            }
            
            .start-btn:hover {
                transform: translateY(-2px);
                box-shadow: 0 8px 25px rgba(107, 70, 193, 0.3);
                color: white;
            }
            
            .exit-btn {
                background: transparent;
                color: #64748b;
                border: 2px solid #e2e8f0;
                padding: 15px 30px;
                font-size: 16px;
                font-weight: 500;
                border-radius: 8px;
                cursor: pointer;
                width: 100%;
                transition: all 0.3s ease;
            }
            
            .exit-btn:hover {
                border-color: #cbd5e1;
                background: #f8fafc;
                color: #64748b;
            }
            
            .section-title {
                color: #1e293b;
                font-size: 24px;
                font-weight: 600;
                margin-bottom: 15px;
            }
            
            .section-text {
                color: #64748b;
                line-height: 1.6;
                margin-bottom: 15px;
            }
            
            .sidebar-title {
                color: #1e293b;
                font-size: 18px;
                font-weight: 600;
                margin-bottom: 10px;
            }
            
            .sidebar-subtitle {
                color: #1e293b;
                font-size: 16px;
                font-weight: 600;
                margin-bottom: 20px;
            }
            
            .sidebar-text {
                color: #64748b;
                font-size: 14px;
                line-height: 1.6;
                margin-bottom: 20px;
                font-style: italic;
            }
            
            .about-link {
                color: #3b82f6;
                text-decoration: none;
                font-weight: 600;
                font-size: 14px;
            }
            
            .about-link:hover {
                text-decoration: underline;
            }
            
            .footer-section {
                background: #1e293b;
                color: #94a3b8;
                padding: 20px;
                text-align: center;
                font-size: 12px;
                margin-top: 40px;
            }
            
            .blank-page {
                min-height: 60vh;
                display: flex;
                align-items: center;
                justify-content: center;
                background: white;
                border-radius: 12px;
                margin: 20px;
                box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
            }
            
            .blank-content {
                text-align: center;
                color: #64748b;
            }
            
            .back-btn {
                background: #6b46c1;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 8px;
                cursor: pointer;
                margin-top: 20px;
                transition: all 0.3s ease;
            }
            
            .back-btn:hover {
                background: #553c9a;
                color: white;
            }
        </style>
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
"""
