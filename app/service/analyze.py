# this is core logic of api performance analyze
import time 
import requests 

def api_analyze_service(url,total_requests):    # functon that analyze by getting input url 

    times = []
    status_code = None
    server = None
    
    for i in range(total_requests):
        start = time.time()
        
        try:
            response = requests.get(url)
            end = time.time()
            
            response_time = end - start
            times.append(response_time)
            
            # Save status code (same for all usually)
            status_code = response.status_code
            
            # Get server info
            server = response.headers.get('Server', 'Unknown')
        
        except Exception as e:
            print(f"Error: {e}")
    
    # Calculations
    average_time = sum(times) / len(times) if times else 0
    min_time = min(times) if times else 0
    max_time = max(times) if times else 0
    
    # Location (basic placeholder)
    location = "Unknown"   # you can enhance later using IP API
    
    # Final result dictionary
    result = {
        "api_url": url,
        "status_code": status_code,
        "response_time": times[-1] if times else 0,  # last request
        "average_time": average_time,
        "min_time": min_time,
        "max_time": max_time,
        "Total_request_send": total_requests,
        "server": server,
        "location": location
    }
    
    return result