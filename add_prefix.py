import json
import argparse

def add_prefix_to_flow_names(json_path, prefix, output_path):
    with open(json_path, 'r',encoding='utf-8') as f:
        data = json.load(f)
    
    # Update flow names
    for flow in data.get('flows', []):
        flow['name'] = prefix + flow['name']
        
        # Update enter flow actions
        for node in flow.get('nodes', []):
            for action in node.get('actions', []):
                if action.get('type') == 'enter_flow':
                    action['flow']['name'] = prefix + action['flow']['name']
    
    # Update campaign flows
    for campaign in data.get('campaigns', []):
        for event in campaign.get('events', []):
            event['flow']['name'] = prefix + event['flow']['name']
    
    # Update trigger flows
    for trigger in data.get('triggers', []):
        trigger['flow']['name'] = prefix + trigger['flow']['name']
    
    # Save the updated data to the output path
    with open(output_path, 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Add prefix to flow names in JSON file.')
    parser.add_argument('input_path', type=str, help='Path to the input JSON file')
    parser.add_argument('prefix', type=str, help='Prefix to add to the flow names')
    parser.add_argument('output_path', type=str, help='Path to save the modified JSON file')
    
    args = parser.parse_args()
    
    add_prefix_to_flow_names(args.input_path, args.prefix, args.output_path)
